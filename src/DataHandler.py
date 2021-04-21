import os
from glob import glob

import pandas as pd
import pretty_midi
import json
import numpy as np
from fuzzywuzzy import fuzz
import pickle

midi_dir = "../dataset/clean_midi"
metadata_path = "../dataset/lmd_matched/md5_to_paths.json"
all_midi_files = [y for x in os.walk(midi_dir) for y in glob(os.path.join(x[0], '*.mid'))]
all_songs = [(path.split("/")[-1]).split(".mid")[0] for path in all_midi_files]
all_songs_df = pd.DataFrame({"SongName":all_songs})
songname_to_filename_map = {(path.split("/")[-1]).split(".mid")[0]: path for path in all_midi_files}
song_title = "winner takes"
partial_ratios = list(map(lambda x: fuzz.WRatio(song_title.lower(), x.lower()), songname_to_filename_map.keys()))
arg_max = np.argmax(np.array(partial_ratios))
song_name = list(songname_to_filename_map.keys())[arg_max]
song_path = songname_to_filename_map[song_name]
midi_data = pretty_midi.PrettyMIDI(song_path)
print(f"Song name: {song_name} and distance: {partial_ratios[arg_max]}")
print(f"Estimated Tempo: {midi_data.estimate_tempo()}")
print(f"Estimated Beat start: {midi_data.estimate_beat_start()}")