import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

print( "Butterworth Filter Design" )
print( "(1) Lowpass Filter" )
print( "(2) Highpass Filter" )
print( "(3) Bandpass Filter" )
print( "(4) Bandstop Filter" )
filter = eval( input( "Please enter your choice: " ) )

print( "-----------------------------------------" )
if filter == 1 or filter == 2:
	fp = eval( input( "Enter passband edge frequency(Hz): " ) )
	fs = eval( input( "Enter stopband edge frequency(Hz): " ) )
	rp = eval( input( "Enter passband ripple(dB): " ) )
	rs = eval( input( "Enter stopband ripple(dB): " ) )
	Fs = eval( input( "Enter sampling frequency: " ) )	

	wp = 2 * fp / Fs	
	ws = 2 * fs / Fs	
elif filter == 3 or filter == 4:
	fp1 = eval( input( "Enter 1st passband edge frequency(Hz): " ) )
	fp2 = eval( input( "Enter 2nd passband edge frequency(Hz): " ) )
	fs1 = eval( input( "Enter 1st stopband edge frequency(Hz): " ) )
	fs2 = eval( input( "Enter 2nd stopband edge frequency(Hz): " ) )
	rp = eval( input( "Enter passband ripple(dB): " ) )
	rs = eval( input( "Enter stopband ripple(dB): " ) )
	Fs = eval( input( "Enter sampling frequency: " ) )
	
	wp1 = 2 * fp1 / Fs
	wp2 = 2 * fp2 / Fs
	ws1 = 2 * fs1 / Fs
	ws2 = 2 * fs2 / Fs	
else:
	print( "Your choice is not supported!" )
	quit( )

if filter == 1:
	n, wn = signal.buttord( wp, ws, rp, rs )
	b, a = signal.butter( n, wn, 'lowpass' )
elif filter == 2:
	n, wn = signal.buttord( wp, ws, rp, rs )
	b, a = signal.butter( n, wn, 'highpass' )
elif filter == 3:
	n, wn = signal.buttord( [ wp1, wp2 ], [ ws1, ws2 ], rp, rs )
	b, a = signal.butter( n, wn, 'bandpass' )
else:
	n, wn = signal.buttord( [ wp1, wp2 ], [ ws1, ws2 ], rp, rs )
	b, a = signal.butter( n, wn, 'bandstop' )

w, H = signal.freqz( b, a )
magnitude = abs( H )
phase = np.angle( H )

plt.figure( 1 )
plt.plot( w, magnitude )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.figure( 2 )
plt.plot( w, phase )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Phase' )

plt.show( )