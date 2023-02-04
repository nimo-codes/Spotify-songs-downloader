import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy



cid = "CLIENT ID"
csi = "CLIENT SECRET"
parent_dir = "DIRECTORY TO MAKE FOLDERS IN"
songlist = "SONG LISTS PATH "

def downloader(folder_num):
        path = os.path.join(parent_dir, folder_num)
        os.mkdir(path)
        os.chdir(path)
        os.system(f"spotdl download {song_link}")


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csi)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


file = open(f"{songlist}","r")
for song_link in file.readlines():
    if song_link[25:26]=="a":
        dic1 = sp.album(f"{song_link}",market=None)
        folder_album = dic1["name"]
        downloader(folder_album)
    elif song_link[25:26]=="p":
        new_song_link = song_link.split("playlist/")    
        playlist_id = new_song_link[1]
        playlist_id = playlist_id.replace('\n',"")
        dic1 = sp.playlist(f"{playlist_id}",market=None )
        folder_playlist = dic1["name"]
        downloader(folder_playlist)
    elif song_link[25:26]=="t":
        new_song_link = song_link.split("track/")    
        track_id = new_song_link[1]
        track_id = playlist_id.replace('\n',"")
        dic1 = sp.track(f"{track_id}",market=None )
        folder_track = dic1["name"]
        downloader(folder_track)

file.close()