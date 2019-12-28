import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

M = 65
w1 = signal.boxcar( M )
w2 = signal.hamming( M )
w3 = signal.hann( M )
w4 = signal.bartlett( M )
w5 = signal.barthann( M )
w6 = signal.kaiser( M, 14 )

plt.figure( 1 )
plt.plot( w1 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 2 )
plt.plot( w2 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 3 )
plt.plot( w3 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 4 )
plt.plot( w4 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 5 )
plt.plot( w5 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 6 )
plt.plot( w6 )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.show( )