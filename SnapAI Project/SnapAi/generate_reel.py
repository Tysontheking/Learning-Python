# this folder help to generate our images into reel

import os
from text_to_speech import text_to_speech_file

import time
import subprocess

def text_to_speech(folder):
    # print('TTS : ',folder)
    with open(f"user_uploads/{folder}/Description.txt") as f:
        text = f.read()
    # print(text,folder)
    text_to_speech_file(text,folder)

def generate_reel(folder):
    # print('GR : ',folder)
    # Add your reel generation logic here
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -map 0:v:0 -map 1:a:0 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    
    subprocess.run(command, shell=True,check=True)


if __name__ == '__main__':
    while True:
        print("Processing quere")
        with open("done.txt",'r') as f:
            done_folder = f.readlines()
            
            done_folder = [f.strip() for f in done_folder]

        folders = os.listdir('user_uploads')
        for folder in folders:
            if(folder not in done_folder):
                text_to_speech(folder)
                generate_reel(folder)
                with open('done.txt', 'a') as f:
                    f.write(folder + '\n')
        time.sleep(4)
        