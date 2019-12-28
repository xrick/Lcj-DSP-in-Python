import numpy as np
import wave
import struct

file = "beat.wav"			# 檔案名稱

amplitude = 30000           # 振幅
f1 = 20						# 低頻頻率(Hz)
f2 = 200					# 高頻頻率(Hz)
duration = 10				# 時間長度(秒)
fs = 44100				   	# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
num_channels = 1			# 通道數
sampwidth = 2				# 樣本寬度
num_frames = num_samples	# 音框數 = 樣本數
comptype = "NONE"		   	# 壓縮型態
compname = "not compressed" # 無壓縮

t = np.linspace( 0, duration, num_samples, endpoint = False )
x = amplitude * np.cos( 2 * np.pi * f1 * t ) * np.cos( 2 * np.pi * f2 * t )

wav_file = wave.open( file, 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

for s in x :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( ) 