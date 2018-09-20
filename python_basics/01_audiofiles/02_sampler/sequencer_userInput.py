import simpleaudio as sa
import time
import random

"""
An example project in which a rhythmical sequence (one measure, 1 sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4
Instead of using steps to iterate through a sequence, we are checking the time.
We will trigger events based on a timestamp.
------ HANDS-ON TIPS ------
- Run the code, read the code and answer the following question:
  - This script transforms a list of 'sixteenth notes timestamps' into a list of
    regular timestamps.
    In the playback loop, the time difference (currentTime minus startTime)
    is compared to the upcomming timestamp.
    Why is this a more accurate method then the methods used in the examples
    "04_randomNoteDuration.py" and "05_oneSampleSequenceSteps.py"?
    Notate your answer below this line (Dutch is allowed)!
    This tells the script the 'actual' time the sample needs to be played,
    not just how mucht time the script has to wait to play the sample again.
- Alter the code:
  Currently one sample is played. Add another sample to the script.
  When a sample needs to be played, choose one of the two samples
  randomly. CHECK.
  (See the hint about the random package in script "02_timedPlayback".)
- Alter the code:
  Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The timestamps list is emptied using the pop() function.
  (multiple possible solutions) CHECK.
"""

# load 1 audioFile and store it into a list
# note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav"),
            sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav")]

playTimes = int(input('How many times would you like to hear the sequence?'))

bpm = 120
print('BPM is set to ' + str(bpm) + ', you can change it now.')

# set bpm
def setBPM():
    try:
        bpm = int(input("What would you like the BPM to be? "))
    except ValueError:
        print('Please enter an integer. ')
        setBPM()

setBPM()

# calculate the duration of a quarter note
quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

timestamps = []
timestamps16th = [0, 2, 4, 8, 11]

def listMaker():
    # create a list with ‘note timestamps' in 16th at which we should play the sample
    # transform the sixteenthTimestamps to a timestamps list with time values
    for timestamp in timestamps16th:
      timestamps.append(timestamp * sixteenthNoteDuration)

listMaker()
print(timestamps)

noteDurlist = [0.25, 0.5, 0.25, 0.5, 0.5, 1, 1]
newTimestamps = []

def durationsToTimestamps16th(noteDurlist):
    count = 0
    for noteDur in noteDurlist:
        newTimestamps.append(count);
        count = count + noteDur*4;

durationsToTimestamps16th(noteDurlist)
print(newTimestamps)

def playBack():
    # retrieve first timestamp
    # NOTE: pop(0) returns and removes the element at index 0
    timestamp = timestamps.pop(0)
    # retrieve the startime: current time
    startTime = time.time()
    keepPlaying = True
    # play the sequence
    while keepPlaying:
      # retrieve current time
      currentTime = time.time()
      # check if the timestamp's time is passed
      if(currentTime - startTime >= timestamp):
        # play sample
        random.choice(samples).play()

        # if there are timestamps left in the timestamps list
        if timestamps:
          # retrieve the next timestamp
          timestamp = timestamps.pop(0)
        else:
          # list is empty, stop loop
          keepPlaying = False
      else:
        # wait for a very short moment
        time.sleep(0.001)
    print('Playback Over!')

while playTimes > 0:
    listMaker()
    playBack()
    playTimes = playTimes - 1
