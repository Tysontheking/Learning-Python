# this folder help to generate our images into reel

import os

def text_to_speech(folder):
    print('TTS : ',folder)

def generate_reel(folder):
    print('GR : ',folder)


if __name__ == '__main__':
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
    