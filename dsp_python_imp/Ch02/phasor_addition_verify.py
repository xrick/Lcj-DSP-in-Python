import numpy as np

phasor1 = complex( 3 * np.cos( np.pi / 4 ), 3 * np.sin( np.pi / 4 ) )
phasor2 = complex( 4 * np.cos( 3 * np.pi / 4 ), 4 * np.sin( 3 * np.pi / 4 ) )
phasor = phasor1 + phasor2

A = abs( phasor )					
phi = np.angle( phasor ) 

print( "Phasor1 =", phasor1 )
print( "Phasor2 =", phasor2 )
print( "Phasor =", phasor )
print( "Amplitude =", A )
print( "Phase Angle =", phi )