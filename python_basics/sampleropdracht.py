## imported modules
import numpy as np
import simpleaudio as sa
import wave
import time

#global variables
wavefile = sa.WaveObject.from_wave_file('/Users/maxschellekens/CSD2/python_basics/bass.wav')
numPlayBackTimes = int(input('Voer in hoe vaak u de sample wil horen en druk op Enter '))

PlayBackArray = []

#Making the Array with note values
i = numPlayBackTimes
while i > 0:
    arrayadd = float(input('Voer je ritmedata in '))
    PlayBackArray.append(float(arrayadd))
    print(str(i - 1) + ' More To Go')
    i = i - 1

print(PlayBackArray)

#Input for BPM
BPMinput = int(input('Voer nu het aantal BPM in en druk op enter '))
print(BPMinput)

#Playing back the sample
p = 0
i = numPlayBackTimes
while i > 0:
    play_obj = wavefile.play()
    time.sleep((60/BPMinput)*PlayBackArray[p])
    play_obj.stop()
    p = p + 1
    i = i - 1


# start playback
