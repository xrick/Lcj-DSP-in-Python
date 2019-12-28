import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def resampling( x, sampling_rate ):
	num = int( len(x) * sampling_rate )
	y = signal.resample( x, num )
	return y

def main( ):
	x = np.array( [ 1, 2, 4, 3, 2, 1, 2, 1 ] )
	y = resampling( x, 1.5 )
	
	plt.figure( 1 )
	plt.stem( x )
	
	plt.figure( 2 )
	plt.stem( y )
	
	plt.show( )
	
main( )	