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
upper_limit = roundup(saved.total, res_limit)

for offset in range(res_limit, upper_limit + res_limit, res_limit):
    # print(offset)
    all_tracks += saved.items
    saved = spotify.saved_tracks(offset=offset, limit=res_limit)

assert len(all_tracks) == saved.total

all_tracks = sorted(all_tracks, key=lambda track: track.track.popularity)

for track in all_tracks:
    print(track.track)