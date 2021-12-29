import tkinter as tk
import scipy.io.wavfile as sc
from pydub import AudioSegment
import os
import filetype as ft

def convertToWav(input_file) -> str: 
    if not input_file.endswith('.mp3'):
        raise 'File format must be mp3' 
        
    output_file = f'./SongsWav/{input_file[:-4]}.wav'
    input = f'./Songs/{input_file}'
    sound = AudioSegment.from_mp3(input)
    sound.export(output_file, format='wav')



convertToWav('03 Kickdown.mp3')



#input_file = './Songs/01 Dwa Trzynas cie.mp3'
#output_file = './SongsWav/01 Dwa Trzynas cie.wav'