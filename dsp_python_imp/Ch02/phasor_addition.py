import numpy as np
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 1000, endpoint = False )			# 定義時間陣列
x1 = 3 * np.cos( 2 * np.pi * 10 * t + np.pi / 4 )		# 第一個弦波
x2 = 4 * np.cos( 2 * np.pi * 10 * t + 3 * np.pi / 4 )	# 第二個弦波
x3 = x1 + x2											# 弦波相加

plt.plot( t, x1, '--', label = 'x1(t)' )				# 繪圖
plt.plot( t, x2, '--', label = 'x2(t)' )
plt.plot( t, x3, '-', label = 'x3(t)' )

plt.legend( loc = 'upper right' )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -6, 6 ] )

plt.show( )