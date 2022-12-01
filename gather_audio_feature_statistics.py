import sys

import tekore as tk


def roundup(x, round_to):
    return x if x % round_to == 0 else x + round_to - x % round_to


# scope = input("Enter the scope for which you wish to request access:\n")
scope = "user_library_read"

conf = tk.config_from_file(f'tekore_{scope}.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(user_token)

all_tracks = []

res_limit = 50
saved = spotify.saved_tracks(limit=res_limit)
# print(saved.items)
# total_tracks = saved.total
upper_limit = roundup(saved.total+res_limit, res_limit)

for offset in range(res_limit, upper_limit, res_limit):
    # print(offset)
    all_tracks += saved.items
    saved = spotify.saved_tracks(offset=offset, limit=res_limit)

assert len(all_tracks) == saved.total


# all_tracks = sorted(all_tracks, key=lambda track: track.track.popularity)

with open('relevant_features.txt','r') as fp:
    audio_features = {k.strip():[] for k in fp}



afs = []

rate_limit = 100
track_ids = [track.track.id for track in all_tracks]
for chunk in range(rate_limit, upper_limit, rate_limit):
    afs += spotify.tracks_audio_features(track_ids[chunk - rate_limit:chunk])
#
for af in afs:
    for f in audio_features:
        audio_features[f].append(getattr(af, f))
#
# print(audio_features)
print(audio_features)
