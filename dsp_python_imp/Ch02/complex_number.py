import numpy as np

z = 3 + 4j							# 定義複數
magnitude = abs( z )				# 計算強度(Magnitude)
theta = np.angle( z ) * 180 / np.pi	# 計算相位角(Phase Angle)

print( "z =", z )
print( "Magnitude =", magnitude )
print( "Phase Angle =", theta )