import glob
from functools import reduce

import librosa.display
import pretty_midi as pm
import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt

"""[IMPORTANT]
/Users/Pushkar/miniconda3/envs/epfl/lib/python3.8/site-packages/pretty_midi/pretty_midi.py:97: 
RuntimeWarning: Tempo, Key or Time signature change events found on non-zero tracks.  
This is not a valid type 0 or type 1 MIDI file.  Tempo, Key or Time Signature may be wrong.
  warnings.warn(
"""
path = "../dataset/clean_midi/Backstreet Boys/" + '*.mid'


def num_instruments():
    songs = glob.glob(path)
    num_instruments = []
    for song_path in songs:
        try:
            mid_track = pm.PrettyMIDI(song_path)
        except:
            continue
        num_instruments.append(len(mid_track.instruments))
    fig = px.histogram(pd.DataFrame({"Total Instruments":num_instruments}))
    fig.show()


def instrument_class(program_number, is_drum, name):
    # https://en.wikipedia.org/wiki/General_MIDI#Parameter_interpretations
    if is_drum:
        return "Percussion"
    if program_number == 0 and "drum" in name.lower():
        return "Percussion"
    if program_number == 0:
        return name
    if 0 < program_number <= 8:
        return "Piano"
    if 8 < program_number <= 16:
        return "Chromatic Percussion"
    if 16 < program_number <= 24:
        return "Organ"
    if 24 < program_number <= 32:
        return "Guitar"
    if 32 < program_number <= 40:
        return "Bass"
    if 40 < program_number <= 48:
        return "Strings"
    if 48 < program_number <= 56:
        return "Ensemble"
    if 56 < program_number <= 64:
        return "Brass"
    if 64 < program_number <= 72:
        return "Reed"
    if 72 < program_number <= 80:
        return "Pipe"
    if 80 < program_number <= 88:
        return "Synth Lead"
    if 88 < program_number <= 96:
        return "Synth Pad"
    if 96 < program_number <= 104:
        return "Synth Effect"
    if 104 < program_number <= 112:
        return "Ethnic"
    if 112 < program_number <= 120:
        return "Percussion"
    if 120 < program_number <= 128:
        return "Sound Effects"


def top_4_instruments():
    songs = glob.glob(path)
    all_ins_durations = []
    for song_path in songs:
        try:
            mid_track = pm.PrettyMIDI(song_path)
        except:
            continue
        instrument_durations = []
        for i, inst in enumerate(mid_track.instruments):
            total_duration = sum(map(lambda a: (a.end-a.start), inst.notes))
            instrument_durations.append({"program":inst.program, "duration":total_duration, "is_drum":inst.is_drum, "name":inst.name})
        instrument_durations = sorted(instrument_durations, key=lambda x: x["duration"], reverse=True)
        all_ins_durations.append(instrument_durations[0:6])
    top_instruments = list(map(lambda x: list(map(lambda y: instrument_class(y["program"], y["is_drum"], y["name"]), x)), all_ins_durations))
    top_instruments = [item for sublist in top_instruments for item in sublist]
    fig = px.histogram(pd.DataFrame({"Top Instruments":top_instruments}))
    fig.show()


def plot_tempo():
    songs = glob.glob(path)
    song_tempos = []
    for song_path in songs:
        try:
            mid_track = pm.PrettyMIDI(song_path)
        except:
            continue
        song_tempos.append(mid_track.estimate_tempo())
    fig = px.histogram(pd.DataFrame({"Tempo":song_tempos}))
    fig.show()


def plot_meter():
    songs = glob.glob(path)
    time_signatures = []
    for song_path in songs:
        try:
            mid_track = pm.PrettyMIDI(song_path)
        except:
            continue
        time_signature_changes = mid_track.time_signature_changes
        try:
            time_signature = str(time_signature_changes[0].numerator)+"/"+str(time_signature_changes[0].denominator)
        except:
            time_signature = "Unknown"
        time_signatures.append(time_signature)
    fig = px.histogram(pd.DataFrame({"Time Signatures":time_signatures}))
    fig.show()



def plot_piano_roll(mid, start_pitch, end_pitch, fs=100):
    # Use librosa's specshow function for displaying the piano roll
    librosa.display.specshow(mid.get_piano_roll(fs)[start_pitch:end_pitch],
                             hop_length=1, sr=fs, x_axis='time', y_axis='cqt_note',
                             fmin=pm.note_number_to_hz(start_pitch))


def plot_first_onset():
    songs = ["/Users/Pushkar/PycharmProjects/Tresillo/dataset/clean_midi/Pink Floyd/Have a Cigar.mid",
             "/Users/Pushkar/PycharmProjects/Tresillo/dataset/clean_midi/Pink Floyd/Hey You.mid"]

    for song_path in songs:
        try:
            mid_track = pm.PrettyMIDI(song_path)
        except:
            continue

        plt.figure(figsize=(8, 4))
        plot_piano_roll(mid_track, 0, 100)
        plt.show()


def accuracy():
    # TODO in the notebook
    pass

plot_meter()