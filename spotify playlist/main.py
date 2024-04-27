import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "80e5fcad1d504ac7bf46c7b1ae30c5c4",
        client_secret="33944006869242f7b0aa5a209f1a11cd",
        show_dialog=True,
        cache_path="token.txt",
        username="http://example.com" ,
    )
)
user_id = sp.current_user()["id"]

