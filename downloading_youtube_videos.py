# -*- coding: utf-8 -*-
"""Downloading_youtube_videos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12_uZHk4Zws6Owtur382AMhWngjWKxcMH
"""

!pip install pytube
!pip install tk

import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def Download(url):
  yt = YouTube(url)
  yt.streams
  yt.streams.filter(progressive=True)
  yt.streams.filter(adaptive=True)
  yt.streams.filter(only_audio=True)
  yt.streams.filter(file_extension='mp4')
  stream = yt.streams.get_by_itag(22)
  stream.download()

url = 'https://www.youtube.com/watch?v=8-agl9TRBwM'
Download(url)