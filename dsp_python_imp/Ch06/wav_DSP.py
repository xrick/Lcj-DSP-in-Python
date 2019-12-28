import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct

def main( ):
	infile  = input( "Input File: " )	
	outfile = input( "Output File: " )
	
	# ----------------------------------------------------
	#  輸入模組
	# ----------------------------------------------------	
	wav = wave.open( infile, 'rb' )
	num_channels = wav.getnchannels( )	# 通道數
	sampwidth	 = wav.getsampwidth( )	# 樣本寬度
	fs			 = wav.getframerate( )	# 取樣頻率(Hz)
	num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
	comptype	 = wav.getcomptype( )	# 壓縮型態
	compname	 = wav.getcompname( )	# 無壓縮
	wav.close( )

	sampling_rate, x = read( infile )	# 輸入訊號

	# ----------------------------------------------------
	#  DSP 模組
	# ----------------------------------------------------	
	y = x

	# ----------------------------------------------------
	#  輸出模組
	# ----------------------------------------------------		
	wav_file = wave.open( outfile, 'w' )
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

	for s in y:
		wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

	wav_file.close( ) 
	
main( )