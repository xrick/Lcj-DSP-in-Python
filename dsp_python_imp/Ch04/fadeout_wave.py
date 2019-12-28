import numpy as np
import wave
import struct

file = "fadeout.wav"		# 檔案名稱

amplitude = 30000           # 音量大小
frequency = 300				# 頻率(Hz)
duration = 3				# 時間長度(秒)
fs = 44100				   	# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"		   	# 壓縮型態
compname = "not compressed" # 無壓縮

t = np.linspace( 0, duration, num_samples, endpoint = False )
a = np.linspace( 1, 0, num_samples, endpoint = False )
x = amplitude * a * np.cos( 2 * np.pi * frequency * t )

wav_file = wave.open( file, 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

for s in x :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( ) 