# README.md

## Overview
Download a YouTube video and extract frames for analysis.

## Installation

1. Install python 3.x

2. Verify CLT installed
    `brew config` and check for CLT not 'N/A' if so, 
    `xcode-select --install`

3. Install the latest version of OpenCV.
_Note, this will take a awhile as homebrew downaloads and compiles the source and all supportiung libraries_

`brew install opencv`

## Project setup

1. create a project dir
    ` mkdir ~/projects/xxx`

2. Setup a python virtual env (3.6.4)

3. install python libs
    `pip install numpy`
    `pip install matplotlib`

4. Activate python env and verify setup
    
    ```
    >source ./env/bin/activate
    (env)>python
    Python 3.7.2 (default, Jan 13 2019, 12:50:01)
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cv2
    >>> import numpy as np
    >>> import matplotlib as mplot
    >>>
    ```

## Usage

1. Download a subject file for analysis (note, may be 100MB+)
    `(env)>python download_video <youtube_url>`

2. Extract frames for review
    `(env)>python extract_frames.py <path>`

3. Examine images in ./data folder


