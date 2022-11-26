import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx} {track['artists'][0]['name']} - {track['name']}")