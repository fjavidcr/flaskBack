import json
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# with open('client_secret/client_secret_spotify.json', 'r') as file:
#     spotify_secrets = json.load(file)

# __CID = spotify_secrets['flaskback']['client_id']
# __SECRET = spotify_secrets['flaskback']['client_secret']

# client_credentials_manager = SpotifyClientCredentials(
#     client_id=__CID, client_secret=__SECRET)

# sp = spotipy.Spotify(
#     client_credentials_manager=client_credentials_manager)


# ranges = ['short_term', 'medium_term', 'long_term']
# for range in ranges:
#     print("range:", range)
#     results = sp.current_user_top_tracks(time_range=range, limit=50)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], '//', item['artists'][0]['name'])
#     print()


import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print("range:", range)
        results = sp.current_user_top_tracks(time_range=range, limit=1)
        for i, item in enumerate(results['items']):
            print(i, item['name'], '//', item['artists'][0]['name'])
            print(json.dumps(item))
        print()

else:
    print("Can't get token for", username)
