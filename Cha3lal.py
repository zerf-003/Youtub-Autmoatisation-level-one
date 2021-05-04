#!/usr/bin/python3.8

import requests as req
import os,sys
try:
    import colorama
except ModuleNotFoundError:
    pass
from colorama import Fore,init
try:
    import subprocess 
except ModuleNotFoundError:
    os.system('pip3 install subprocess')
try:
    import pytube
except ModuleNotFoundError:
    os.system('pip3 install pytube')

try:
    import subprocess
except ModuleNotFoundError:
    os.system('pip3 insatall subprocess')

from pytube import YouTube
from pytube.cli import on_progress
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
    for ___ in videos.items():
        aaa = videos.get('items')
        my_all = dict(aaa[0])
        for ___ in my_all.items():
            main = my_all.get('snippet')
            for ___ in main.items():
                link = main.get('resourceId')
                i_d = link.get('videoId')
                final_link = 'https://www.youtube.com/watch?v={}'.format(str(i_d))
                final_title = main.get('title')
                print("""
                    [+] Last Video Of Teacher Sidahmed Cha3lal Is ===> {}
                    
                    [+] Video Link ===> {}""".format(final_title, final_link))
                download = input('[+] Do You Want To Donwload It (Y/N): ')
                if download == "y" or download == 'Y':
                    print('[+] Downloading...' + Fore.GREEN)
                    yt = pytube.YouTube(str(final_link), on_progress_callback=on_progress)
                    yt = yt.streams.get_highest_resolution()
                    yt.download()
                    var = subprocess.Popen(['vlc', final_title+'mp4'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                    
                else:
                    print("Thanks Bro See U soon")

                
                break
            break
        break


get_last_video('UCY-8yXDXiN9MJx6v2Z53HFw')

