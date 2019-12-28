import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

n = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
x = np.array( [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] )

b = np.array( [ 1 ] )
a = np.array( [ 1, -0.8 ] )
y = signal.lfilter( b, a, x )

print( "x =", x )
print( "y =", y )

plt.figure( 1 )
plt.stem( n, x )
plt.xlabel( 'n' )
plt.ylabel( 'x[n]' )

plt.figure( 2 )
plt.stem( n, y )
plt.xlabel( 'n' )
plt.ylabel( 'y[n]' )

plt.show( )