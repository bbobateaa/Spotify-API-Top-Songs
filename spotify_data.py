# Helen Chau
# chauh4@uci.edu
# 84334175

import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials as sc


def spotify_data(artist):
    ''' Created spotify_data function to receive
    data about artist and their top songs
    using the Spotify API '''
    try:
        # Using Spotify API and assigning it to a variable
        c_id = "ca03418c564d4322be338670f94239ce"
        c_s = "SPOTIFY CODE"
        spot = sp.Spotify(auth_manager=sc(client_id=c_id,
                                          client_secret=c_s))
        # Getting data from given artist using search
        results = spot.search(artist)

        # Made dictionary for data collecting
        popular = {}

        # Iterating through data to get artist's url
        for track in results['tracks']['items']:
            info = track['album']['artists'][0]
            info = info['external_urls']
            artist_url = info['spotify']

        # Using artist's url to find their top tracks
        top_songs = spot.artist_top_tracks(artist_url)
        # Iterates through top_songs to find name of songs
        for song in top_songs['tracks']:
            # Assigning song name with its popularity score
            popular[song['name']] = song['popularity']
        # Creating text file to write data to
        with open("datafile.txt", "w") as myfile:
            # Writing artist name for bar graph title
            myfile.write(f"{artist}\n")
            # Iterates through popular dictionary
            for line in popular:
                # Writes each song title with its popularity score in file
                myfile.writelines(f'{line}//popularity//{popular[line]}\n')
        # Returns True after finishingå
        return True
    # Returns False, meaning user entered invalid artist
    except NameError:
        return False
    except TypeError:
        return False
    except KeyError:
        return False
