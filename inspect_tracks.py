import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()

print(results.get('items')[0].keys())