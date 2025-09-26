from midiutil import MIDIFile
import random

track    = 0
channel  = 0
time     = 0     
duration = 1     
tempo    = 120   
volume   = 100   


midi = MIDIFile(1)
midi.addTempo(track, time, tempo)

notes = [60, 62, 64, 65, 67, 69, 71, 72]  

for i in range(20):
    note = random.choice(notes)
    midi.addNote(track, channel, note, time + i, duration, volume)

with open("random_music.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("🎶A music file has been created random_music.mid")
