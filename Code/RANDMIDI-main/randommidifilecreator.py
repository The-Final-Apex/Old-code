import mido
from mido import Message, MidiFile, MidiTrack
import random

# List of possible piano notes
notes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86]

# Create a new MIDI file and a track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add 16 random notes to the track
for i in range(16):
    note = random.choice(notes)
    track.append(Message('note_on', note=note, velocity=64, time=32))
    track.append(Message('note_off', note=note, velocity=64, time=32))

# Save the MIDI file
mid.save('random_piano_song.mid')