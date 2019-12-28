import numpy as np
from numpy.fft import fft, fftshift, ifft, fftfreq
import matplotlib.pyplot as plt

def ideal_lowpass_filtering( x, cutoff, fs ):
	X = fft( x )
	H = np.zeros( fs )
	for i in range( -cutoff, cutoff + 1 ):
		H[i] = 1	
	Y = H * X
	y = ifft( Y )
	y = y.real
	return y

def ideal_highpass_filtering( x, cutoff, fs ):
	X = fft( x )
	H = np.zeros( fs )
	for i in range( -cutoff, cutoff + 1 ):
		H[i] = 1	
	H = 1 - H
	Y = H * X
	y = ifft( Y )
	y = y.real
	return y

def ideal_bandpass_filtering( x, f1, f2, fs ):
	X = fft( x )
	H = np.zeros( fs )
	for i in range( f1, f2 + 1 ):
		H[i] = 1	
	for i in range( -f1, -f2 - 1, -1 ):
		H[i] = 1
	Y = H * X
	y = ifft( Y )
	y = y.real
	return y

def ideal_bandstop_filtering( x, f1, f2, fs ):
	X = fft( x )
	H = np.zeros( fs )
	for i in range( f1, f2 + 1 ):
		H[i] = 1	
	for i in range( -f1, -f2 - 1, -1 ):
		H[i] = 1
	H = 1 - H
	Y = H * X
	y = ifft( Y )
	y = y.real
	return y	

def ideal_allpass_filtering( x ):
	X = fft( x )
	Y = X
	y = ifft( Y )
	y = y.real
	return y	
	
def main( ):
	print( "DSP in Frequency Domain" )
	print( "(1) Ideal Lowpass Filtering" )
	print( "(2) Ideal Highpass Filtering" )
	print( "(3) Ideal Bandpass Filtering" )
	print( "(4) Ideal Bandstop Filtering" )
	print( "(5) Ideal Allpass Filtering" )
	
	choice = eval( input( "Please enter your choice: " ) )

	if choice == 1 or choice == 2:
		fc = eval( input( "Please enter cutoff frequency(Hz): " ) )
		
	if choice == 3 or choice == 4:
		f1 = eval( input( "Please enter frequency f1(Hz): " ) )
		f2 = eval( input( "Please enter frequency f2(Hz): " ) )
	
	fs = 500
	t = np.linspace( 0, 1, fs, endpoint = False )
	x = np.cos( 2 * np.pi * 10 * t ) + np.cos( 2 * np.pi * 20 * t ) + np.cos( 2 * np.pi * 30 * t )

	if choice == 1:
		y = ideal_lowpass_filtering( x, fc, fs )
	elif choice == 2:
		y = ideal_highpass_filtering( x, fc, fs )
	elif choice == 3:
		y = ideal_bandpass_filtering( x, f1, f2, fs )
	elif choice == 4:
		y = ideal_bandstop_filtering( x, f1, f2, fs )
	else:
		y = ideal_allpass_filtering( x )
	
	f = fftshift( fftfreq( fs, 1 / fs ) )
	Xm = abs( fftshift( fft( x ) ) )
	Ym = abs( fftshift( fft( y ) ) )
	
	plt.figure( 1 )
	plt.plot( x )
	plt.xlabel( 't (second)' )
	plt.ylabel( 'Amplitude' )

	plt.figure( 2 )
	plt.plot( f, Xm )
	plt.xlabel( 'f' )
	plt.ylabel( 'Magnitude' )	

	plt.figure( 3 )
	plt.plot( y )
	plt.xlabel( 't (second)' )
	plt.ylabel( 'Amplitude' )	

	plt.figure( 4 )
	plt.plot( f, Ym )
	plt.xlabel( 'f' )
	plt.ylabel( 'Magnitude' )			
	
	plt.show( )
	
main( )