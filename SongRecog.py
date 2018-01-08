import os, sys, json, wave
from acrcloud.recognizer import ACRCloudRecognizer, ACRCloudRecognizeType
from pathlib import Path

def recog():file.wav
    SONG_PATH = 'xxxxxxxxxxxxxxxx'

    if Path(SONG_PATH).is_file():
        SONG_NAME = 'file.wav'
        
        config = {
            'host':'xxxxxxx',
                'access_key':'xxxxxx',
                'access_secret':'xxxxxxx',
                'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
                'debug':False,
                'timeout':10 # seconds
        }
        
        re = ACRCloudRecognizer(config)
        
        details = json.loads(re.recognize_by_file(SONG_NAME, 0, 10))
        
        if len(details) == 1:
            print('Error: Could not recognize song')
            return ''
        else:
            artist = details.get('metadata').get('music')[0].get('artists')[0].get('name')
            title = details.get('metadata').get('music')[0].get('title')
            return artist + " " + title
        os.remove(SONG_PATH)
    else:
        print('Error: Recording not found')
        return ''
