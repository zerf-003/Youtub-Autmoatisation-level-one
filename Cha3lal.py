#!/usr/bin/python3.8
#coded by Billal

import requests as req
import os,sys
try:
    import subprocess 
except ModuleNotFoundError:
    os.system('pip install subprocess')

from apiclient.discovery import build


#initialize youtube key APi
api_key = 'AIzaSyDCHRUU0s5p4-e-BqB6EKxw2W4RFKnT4xA'
youtube = build('youtube', 'v3',developerKey=api_key)

#specify  Cha3lal Channel
channel = youtube.channels().list(id="UCY-8yXDXiN9MJx6v2Z53HFw", part='contentDetails').execute()
videos = youtube.playlistItems().list(playlistId="UUY-8yXDXiN9MJx6v2Z53HFw",part='snippet', maxResults=50).execute()

#Get the last video of Cha3lal Channel
def get_last_video(id):
    channel = youtube.channels().list(id=id, part='contentDetails').execute()
    play_list = channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = youtube.playlistItems().list(playlistId=play_list,part='snippet', maxResults=50).execute()
    videos = dict(videos) 
    for i in videos['items']:
        a = i['snippet']
        title = a['title']
        print(title)
    
get_last_video('UCY-8yXDXiN9MJx6v2Z53HFw')