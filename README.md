# SpotifyHotkeyPy

A simple utility to save the currently playing song on Spotify to your library.

# Usage
**Create an application on Spotify's developer console:**  
https://developer.spotify.com/dashboard/applications

1. Run `$python main.py` to generate a `config.json` if you don't have one.
2. In your spotify app, register a redirect URI for auth
    - Dashboard > Your application > Edit Settings > Redirect URIs > Add > Save
    - The default and recommended value is `http://localhost:5000/callback` but any localhost URI will do
3. In `config.json`, replace `auth_callback_uri` with your redirect URI, replace `client_id` with your app's client_id, replace `client_secret` with your app's client_secret.
4. Optionally, replace the default hotkey. Special keys should be in angle brackets (e.x. `<ctrl>` for ctrl)
5. Re-run `$python main.py`. You should be redirected to your browser to authorize your app with the appropriate scopes.
6. That's it! Just press your hotkey to save the current song.

# Credits
- [Spotify API](https://developer.spotify.com/)
- [Pynput](https://pypi.org/project/pynput/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
