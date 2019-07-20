# # Beat tracking example
# from __future__ import print_function
# import librosa

# # 1. Get the file path to the included audio example
# filename = "res/idaho.mp3"

# # 2. Load the audio as a waveform `y`
# #    Store the sampling rate as `sr`
# y, sr = librosa.load(filename)

# # 3. Run the default beat tracker
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# print(beat_frames)

# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# # 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#############################################################################
#									    #
#			Musical Note Identification			    #
#									    #
#############################################################################

# import numpy as np
# import wave
# import struct


# sampling_freq = 44100	#Sampling frequency of audio signal
# window = 2205           #Size of window to be used for detecting silence
# threshold = 600         #threshold value
# dft = []                #array to store dtf value
# start = []              #array holding start indices of each note
# end = []                #array holding end   indices of each note
# Identified_Notes = []   #list of identified notes

# array = [1046.50, 1174.66, 1318.51, 1396.91, 1567.98, 1760.00, 1975.53,
#          2093.00, 2349.32, 2637.02, 2793.83, 3135.96, 3520.00, 3951.07,
#          4186.01, 4698.63, 5274.04, 5587.65, 6271.93, 7040.00, 7902.13]

# notes = ['C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6',
#          'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7',
#          'C8', 'D8', 'E8', 'F8', 'G8', 'A8', 'B8']


# def play(sound_file):

#     Identified_Notes[:] = []                #Clear the list every time play() is called
#     start[:] = []
#     end[:] = []
    
#     file_length = sound_file.getnframes()   #Decode Audio File       
#     sound = np.zeros(file_length)

#     for i in range(file_length):
#         data = sound_file.readframes(1)
#         data = struct.unpack("<h", data)
#         sound[i] = int(data[0])

#     sound = np.divide(sound, float(2**15))

#     sound_square = np.square(sound)         #square each element of sound[]
    
#     i = 0
#     j = 0
#     f = 0
#     t = 0
    
#     while(i<(file_length) - window):
#         s = 0.00
#         j = 0
#         if(t==0):
#             start.append(i)                 #store start point of note
#             f = 0
#             t = 1 
#         while(j<=window):
#             s = s + sound_square[i + j]
#             j = j + 1
#         if(s<=threshold):
#             if(f==0):
#                 end.append(i)               #store end point of note
#                 f = 1
#         else:
#             if(f==1):
#                 f = 0
#                 t = 0
#         i = i + window

#     i = 0
    
#     while(i<len(end)):                      #Identify Notes
#         dft = np.array(np.fft.fft(sound[start[i]:end[i]]))  # applying fourier transform function
#         dft = np.argsort(dft)
#         if(dft[0]>dft[-1] and dft[1]>dft[-1]):
#             i_max = dft[-1]
#         elif(dft[1]>dft[0] and dft[-1]>dft[0]):
#             i_max = dft[0]
#         else:
#             i_max = dft[1]
#         fr = (i_max*sampling_freq)/((end[i]) - (start[i]))   # claculating frequency
#         idx = (np.abs(array-fr)).argmin()
#         Identified_Notes.append(notes[idx])
#         i = i + 1
        
#     print(Identified_Notes)


# ############################## Read Audio File #############################

# if __name__ == "__main__":
    
#     #code for checking output for single audio file
#     #Reading audio file

#     #code for checking output for remaining all audio files
#     file_name = "res/idaho.wav"
#     sound_file = wave.open(file_name)
#     play(sound_file)

idaho = "3,1,5,4,4,3,2,6,7,2"
testStr = "FMEJEIEHGH"
newStr = ""
i = 0
for num_ch in idaho.split(','):
    num = int(num_ch)
    newStr += chr(ord(testStr[i]) + num)
    i += 1

print(newStr)