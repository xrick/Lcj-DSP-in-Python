import numpy as np
import wave
import struct

def note( pitch, beat ):
	fs = 44000
	amplitude = 30000
	frequency = np.array( [ 261.6, 293.7, 329.6, 349.2, 392.0, 440.0, 493.9 ] )
	num_samples = beat * fs
	t = np.linspace( 0, beat, num_samples, endpoint = False )
	a = np.linspace( 0, 1, num_samples, endpoint = False )
	x = amplitude * a * np.cos( 2 * np.pi * frequency[ pitch - 1 ] * t )
	return x

def main():
	file = "little_bee.wav"	# 檔案名稱

	pitches = np.array( [ 5, 3, 3, 4, 2, 2, 1, 2, 3, 4, 5, 5, 5,    \
					      5, 3, 3, 4, 2, 2, 1, 3, 5, 5, 3,          \
						  2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 3, 3, 4, 5, \
						  5, 3, 3, 4, 2, 2, 1, 3, 5, 5, 1 ] )

	beats = np.array( [ 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,    \
						1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4,          \
						1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, \
						1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4 ] )

	tempo = 0.5					# 節奏(每拍0.5秒)
	fs = 44000
	duration = sum( beats ) * tempo
	num_samples = int( duration * fs )
	
	num_channels = 1			# 通道數
	samwidth = 2				# 樣本寬度
	num_frames = num_samples	# 音框數 = 樣本數
	comptype = "NONE"		   	# 壓縮型態
	compname = "not compressed" # 無壓縮

	num_notes = np.size( pitches )

	y = np.array( [ ] )
	for i in range( num_notes ):
		x = note( pitches[i], beats[i] * tempo )
		y = np.append( y, x )

	wav_file = wave.open( file, 'w' )
	wav_file.setparams(( num_channels, samwidth, fs, num_frames, comptype, compname ))

	for s in y:
		wav_file.writeframes( struct.pack( 'h', int( s ) ) )

	wav_file.close( )		

main()