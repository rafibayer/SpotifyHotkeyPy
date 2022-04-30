# Author: Rafael Bayer (https://github.com/rafibayer)

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import Config
from pynput import keyboard

SPOTIFY_AUTH_SCOPE = "user-read-currently-playing user-library-read user-library-modify"

print("loading config from config.json")
config = None

try:
    with open("./config.json", "r") as f:
        config = Config.load(f.read())
except Exception as e:
    print("Error loading config: " + str(e))
    print("Creating new default file: config.json")
    config = Config("id", "secret", "http://localhost:5000/callback", "<ctrl>+<alt>+p")
    with open("config.json", "w+") as f:
        f.write(Config.dump(config))
    exit(1)

print("initializing spotify client")
auth_manager = SpotifyOAuth(
    config.client_id,
    config.client_secret,
    redirect_uri=config.auth_callback_uri,
    scope=SPOTIFY_AUTH_SCOPE)

spotify = spotipy.Spotify(auth_manager=auth_manager)

def on_activate():
    current = spotify.current_user_playing_track()
    if current is None:
        print("No song is playing")
        return

    print(f"Attempting to save: {current['item']['name']} ({current['item']['uri']})")
    if spotify.current_user_saved_tracks_contains([current["item"]["uri"]])[0]:
        print("Song is already saved")
    else:
        print("Saving song")
        spotify.current_user_saved_tracks_add([current["item"]["id"]])

print(f"registering hotkey: {config.hotkey}")
with keyboard.GlobalHotKeys(hotkeys = { config.hotkey: on_activate }) as h:
    h.join()