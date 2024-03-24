import mido
from mido import MidiFile, MidiTrack, Message
import time

# Define a sequence: (note, velocity, delay)
sequence = [
    (60, 64, 0.5),  # Note C4
    (61, 65, 0.5),
    (62, 64, 0.5),  # Note D4
    (64, 64, 0.5),  # Note E4
    (65, 64, 0.5),  # Note F4
    (67, 64, 0.5),  # Note G4
    (69, 64, 0.5),  # Note A4
    (71, 64, 0.5),  # Note B4
    (72, 64, 0.5),  # Note C5
]

# Create a MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Play the sequence
for note, velocity, delay in sequence:
    # Note on
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    time.sleep(delay)  # Delay before note_off
    # Note off
    track.append(Message('note_off', note=note, velocity=velocity, time=0))

# Save the MIDI file
mid.save('sequence.mid')