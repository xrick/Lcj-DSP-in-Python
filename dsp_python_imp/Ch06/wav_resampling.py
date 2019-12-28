import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal

def downsampling( x, method = 1 ):
	N = int( len( x ) / 2 ) 
	y = np.zeros( N )
	
	if method == 1:   			# Decimation 
		for n in range( N ):
			y[n] = x[2*n]
	else:						# Average
		for n in range( N ):
			y[n] = ( x[2*n] + x[2*n+1] ) / 2	
			
	return y
	
def upsampling( x, method = 1 ):
	N = len( x ) * 2
	y = np.zeros( N )	
	
	if method == 1:				# Zero-Order Hold
		for n in range( N ):
			y[n] = x[int( n / 2 )] 
	else:						# Linear Interpolation
		for n in range( N ):
			if int( n / 2 ) == n / 2:
				y[n] = x[int( n / 2 )]
			else:
				n1 = int( n / 2 )
				n2 = n1 + 1
				if n2 < len( x ):
					y[n] = ( x[n1] + x[n2] ) / 2
				else:
					y[n] = x[n1] / 2

	return y

def resampling( x, sampling_rate ):
	num = int( len(x) * sampling_rate )
	y = signal.resample( x, num )
	return y	
	
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
	
	print( "Sampling Rate Conversion" )
	print( "(1) Downsampling by 2 (Decimation)" )
	print( "(2) Downsampling by 2 (Average)" )
	print( "(3) Upsampling by 2 (Zero-Order Hold)" )
	print( "(4) Upsampling by 2 (Linear Interpolation)" )
	print( "(5) Resampling" )
	
	choice = eval( input( "Please enter your choice: " ) )
	
	if choice == 1:
		y = downsampling( x, 1 )
	elif choice == 2:
		y = downsampling( x, 2 )
	elif choice == 3:
		y = upsampling( x, 1 )
	elif choice == 4:
		y = upsampling( x, 2 )
	elif choice == 5:
		sampling_rate = eval( input( "Sampling Rate = " ) )
		y = resampling( x, sampling_rate )
	else:
		print( "Your choice is not supported!" )
		y = x

	num_frames = len( y )
		
	# ----------------------------------------------------
	#  輸出模組
	# ----------------------------------------------------		
	wav_file = wave.open( outfile, 'w' )
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

	for s in y:
		wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

	wav_file.close( ) 
	
main( )