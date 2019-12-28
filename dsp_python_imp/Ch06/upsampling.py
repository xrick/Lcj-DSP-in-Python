import numpy as np
import matplotlib.pyplot as plt

def upsampling( x, method = 1 ):
	N = len( x ) * 2
	y = np.zeros( N )	
	
	if method == 1:				# Zero-Order Hold
		for n in range( N ):
			y[n] = x[int( n / 2 )] 
	else:						# Linear Interpolation
		for n in range( N ):
			if int( n / 2 ) == n / 2:
				y[n] = x[int( n / 2 )]
			else:
				n1 = int( n / 2 )
				n2 = n1 + 1
				if n2 < len( x ):
					y[n] = ( x[n1] + x[n2] ) / 2
				else:
					y[n] = x[n1] / 2

	return y
	
def main( ):
	x = np.array( [ 1, 2, 4, 3, 2, 1, 2, 1 ] )
	y1 = upsampling( x, 1 )
	y2 = upsampling( x, 2 )
	
	plt.figure( 1 )
	plt.stem( x )
	
	plt.figure( 2 )
	plt.stem( y1 )
	
	plt.figure( 3 )
	plt.stem( y2 )
	
	plt.show()

main( )	