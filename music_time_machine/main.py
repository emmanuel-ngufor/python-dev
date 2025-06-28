import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

pp = pprint.PrettyPrinter(indent=0)

client_ID = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
redirect_url = os.environ["SPOTIPY_REDIRECT_URL"]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_ID,
        client_secret=client_secret,
        redirect_uri=redirect_url,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
date = input("What year would you like to create a spotify playlist (please use the YYYY-MM-DD format): ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
