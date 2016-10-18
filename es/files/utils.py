import os, json
from colorme import ColorMe
from collections import OrderedDict
from mutagen.mp3 import EasyMP3
from mutagen.easymp4 import EasyMP4


env = os.environ['HOME']

if 'nick' in env:
    music_dir = '/Users/nick/Music/iTunes/iTunes Media/Music'
    web_dir = 'static/music'
else:
    music_dir = '/mnt/seagatehd/Music'
    web_dir = 'static/music/'

music_dict = {}
meta_dict = OrderedDict()
error_list = []
COUNT = 0
YEAR = ""
fp = open('errors_log.txt', 'w')
fp.close()


def speak(msg, wait=False):
    os.system('echo "%s" | say%s'%(msg, wait and ' ' or ' &'))

def parser(attrib, audio):
    if not attrib in audio:
        audio[attrib] = 'None'
        #audio.save()

def get_year(path):
    if "2012" in path:
        return "2012"
    elif "2013" in path:
        return "2013"
    elif "2015" in path:
        return "2015"
    else:
        return "2015"

def get_ext(link):
    if(link.endswith('.mp3')):
        return EasyMP3(link)
    elif(link.endswith('.m4a')):
        return EasyMP4(link)
    else:
        raise ValueError('Unable to read file extension.')


def color_text(txt, status):
    if status == 'fail':
        print ColorMe.FAIL + txt + ColorMe.ENDC
    elif status == 'success':
        print ColorMe.OKGREEN + txt + ColorMe.ENDC


def json_parse_data(search=None):
    print 'Parsing.....%s '%music_dir
    pk=1
    for root,dirs,files in os.walk(music_dir):
        for name in files:
            full_path = os.path.join(root,name)
            print '#####\npath: ---> %s'%full_path
            try:
                audio = get_ext(full_path)
            except:
                color_text('Unable to parse file.', 'fail')
                with open("errors_log.txt", "a") as myfile:
                    myfile.write(full_path)
                    myfile.write("\n")
                continue
            parser('artist', audio)
            parser('album', audio)
            parser('title', audio)
            entry = {}
            YEAR = get_year(full_path)
            entry = {
                'title': audio['title'][0],
                'artist': audio['artist'][0],
                'album': audio['album'][0],
                'path': full_path.replace(music_dir, web_dir),
                'year': YEAR
            }
            meta_dict = {
                "index": {
                    "_id": str(pk),
                    "_index": "music",
                    "_type": "nick"
                }
            }
            pk += 1
            with open('music.json', 'a+') as f:
                json.dump(meta_dict, f)
                f.write('\n')
                json.dump(entry, f)
                f.write('\n')
            color_text('Successfully parsed file.', 'success')
    print 'Finished parsing data.'


if __name__ == "__main__":
    json_parse_data()
    speak('Write to music.json successfull.')
