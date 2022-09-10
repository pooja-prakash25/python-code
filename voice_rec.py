import sounddevice

from scipy.io.wavfile import write

#frequency of the sound
freq=44100

#recording duration
duration=5

#start recorder with the given freq and durtn
print("Recording......")

record= sounddevice.rec(int(freq*duration),samplerate=freq,channels=2)

sounddevice.wait()

print("DONE!")

write("output.wav",freq,record)