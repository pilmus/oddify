import tekore as tk

# scope = input("Enter the scope for which you wish to request access:\n")
scope = "user_library_read"

conf = tk.config_from_file(f'tekore_{scope}.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])



spotify = tk.Spotify(user_token)

tracks = spotify.saved_tracks().items

track = tracks[0].track
# print(track)
print(track.artists[0])
# print(spotify.track_audio_features(track.id))


print(spotify.artist('4KY9rCrokaoFzvMfX98u1q'))
