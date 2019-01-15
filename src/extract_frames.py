
# -*- coding: utf-8 -*-
"""
Given an input MP4 file, scan the video and extract frames.

"""

import logging
import os
import cv2
import shutil

logger = logging.getLogger(__name__)
 
def extractFrames(input_path, output_path, start_frame=0, max_frames=1000, interval=60):
    
    cap = cv2.VideoCapture(input_path)
    frame_count = 0
    extract_count = 0
 
    while (cap.isOpened() and extract_count < max_frames):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == False:
            break # error?

        if frame_count % interval == 0:
            logger.info('Read %d frame: ' % extract_count, ret)
            cv2.imwrite(os.path.join(output_path, "frame{:d}.jpg".format(extract_count)), frame)  # save frame as JPEG file
            extract_count += 1
        
        frame_count += 1
        
    # once complete, release the capture
    cap.release()
    cv2.destroyAllWindows()
 
def main():

    mp4_file = 'best-starcraft-2-game-ever-p1.mp4'
    work_dir = os.path.join(os.getcwd())
    
    input_path = os.path.normpath(os.path.join(work_dir, 'downloads', mp4_file))
    output_path = os.path.normpath(os.path.join( work_dir, 'data'))

    # clean up from previous run if needed
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    extractFrames(input_path, output_path, start_frame=1000, max_frames=10000, interval=120)
 
if __name__== "__main__":
    main()
