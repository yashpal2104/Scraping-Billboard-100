import requests, pprint, datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all('h3', id='title-of-a-story',
                          class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')


song_names = [song.get_text(strip=True) for song in all_songs]
# print(song_names)


year_to_travel_to = input("Which year do you want me to travel to? Type the date in this format YYYY-MM-DD: ")

client_id = '3f5672e761734c71a0190511073b789a'
client_secret = 'b71e00c833124ce68ca102af2c90914e'
redirect_uri = 'http://example.com'  # The redirect URI you set up in the Spotify Developer Dashboard


# Create a SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope="playlist-modify-private")

# Now you can create a Spotipy client
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Get the current user's profile information
user_profile = sp.current_user()

# Extract the user ID (Spotify username)
user_id = user_profile['id']

print("User ID (Spotify Username):", user_id)

# Example: Get current user's playlists
playlists = sp.current_user_playlists()
for playlist in playlists['items']:
    print(playlist['name'])

# Create a list to store the Spotify URIs
song_uris = []
year = year_to_travel_to.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")




playlist = sp.user_playlist_create(user=user_id, name=f"{year_to_travel_to} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


