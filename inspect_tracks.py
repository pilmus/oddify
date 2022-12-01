import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks(offset=100)

print(len(results.get('items')))

#
#
# print(results.get('items')[0].get('track').get('artists')[0])
#
#
# print(sp.artist('4KY9rCrokaoFzvMfX98u1q'))
#
# print(sp.search(q='artist: ', type='artist'))