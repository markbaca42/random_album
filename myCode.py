import spotipy  
from spotipy.oauth2 import SpotifyOAuth  
from spotipy import Spotify
import json
import numpy as np

# Open the file in read mode
with open('client_id.txt', 'r') as file:
    # Read the contents of the file
    CLIENT_ID = file.read()
with open('client_secret.txt', 'r') as file:
    # Read the contents of the file
    CLIENT_SECRET = file.read()

# Now file_contents contains the contents of the file
print(CLIENT_ID)

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:3000/', scope='user-library-read')  

access_token = sp_oauth.get_access_token()  

sp = Spotify(auth_manager=sp_oauth)  
  
results = sp.current_user_saved_albums(limit=50,offset=50)  

# print(results.dtype)

# # parse x
# data = json.loads(results)
albums = results['items']
# # the result is a Python dictionary:
# print(len(albums))
# print('\n\n')
# album_1 = albums[0]
# keys_list = list(album_1.keys())
# print(album_1['album']['name'])
# for album in(albums):
#     album_name = album['album']['name']
#     print(album_name)

offset = 0
LIMIT = 50
album_array = np.empty((0,))
while(len(albums) > 0):
    results = sp.current_user_saved_albums(limit=LIMIT,offset=offset)  

    # print(results.dtype)

    # # parse x:
    # data = json.loads(results)
    albums = results['items']
    for album in(albums):
        album_name = album['album']['name']
        # print(album_name)
        album_array = np.append(album_array, album_name)
    offset += len(albums)

random_elements = np.random.choice(album_array, size=5, replace=False)

print(random_elements)