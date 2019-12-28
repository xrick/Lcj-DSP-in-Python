import numpy as np
from numpy.fft import fft, fftshift, ifft, fftfreq
import matplotlib.pyplot as plt

def spectrum_shifting( x, shift, fs ):
	X = fft( x )
	N = fs
	N_half = int( fs / 2 )
	Y = np.zeros( N, dtype = 'complex' )
	for i in range( N_half ):
		if i + shift >= 0 and i + shift <= N_half:
			Y[i + shift] = X[i]
	for i in range( N_half + 1, fs ):
		if i - shift >= N_half + 1 and i - shift < N:
			Y[i - shift] = X[i]
	y = ifft( Y )
	y = y.real
	return y
	
def main( ):
	fs = 500
	t = np.linspace( 0, 1, fs, endpoint = False )
	x = np.cos( 2 * np.pi * 50 * t )

	y = spectrum_shifting( x, -30, fs )
	
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