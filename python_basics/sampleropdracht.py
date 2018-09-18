## PlaySound, Test voor SimpleAudio
import numpy as np
import simpleaudio as sa
import time
import wave

#numPlayBackTimes
numPlayBackTimes = int(input('Please input the amount of times you would like to hear the sample and press Enter'))

PlayBackArray = []

#Waarden toevoegen aan PlayBackArray
i = numPlayBackTimes
while i > 0:
    ArrayWaarde = input('Please input length value number')
    print(str(i - 1) + ' more to go')
    PlayBackArray.append(int(ArrayWaarde))
    i = i - 1

print(PlayBackArray)

#Inladen/Bufferen etc

wave_read = wave.open('C:/Users/Max/Documents/CSD2/python_basics/Grungecore.wav', 'rb')
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()

play_obj = sa.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)
play_obj.wait_done()

# start playback
#while i > 0:
#    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
#    play_obj.wait_done()
#    i = i - 1
