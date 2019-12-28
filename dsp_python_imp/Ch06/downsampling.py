import numpy as np
import matplotlib.pyplot as plt

def downsampling( x, method = 1 ):
	N = int( len( x ) / 2 ) 
	y = np.zeros( N )
	
	if method == 1:				# Decimation 
		for n in range( N ):
			y[n] = x[2*n]
	else:						# Average
		for n in range( N ):
			y[n] = ( x[2*n] + x[2*n+1] ) / 2	
			
	return y
		
def main( ):
	x = np.array( [ 1, 2, 4, 3, 2, 1, 2, 1 ] )
	y1 = downsampling( x, 1 )
	y2 = downsampling( x, 2 )
	
	plt.figure( 1 )
	plt.stem( x )
	
	plt.figure( 2 )
	plt.stem( y1 )
	
	plt.figure( 3 )
	plt.stem( y2 )
	
	plt.show()

main( )	