
# -*- coding: utf-8 -*-
""" 
Download a YouTube video for analysis
"""


import logging
import os
import pytube
from pytube import YouTube

logger = logging.getLogger(__name__)

# here is a fun video with lots of StarCraft units 
URL = 'https://www.youtube.com/watch?v=vB5ja3XKl7g'

def main():
    YouTube(URL).streams.first().download()

if __name__=="__main__":
    main()