import SoundRecorder
import SongRecog
import SongsterrFind
import ChordFind
import webbrowser

SoundRecorder.record()
SONG_DETAILS = SongRecog.recog()
FORM = ''

if type(SONG_DETAILS) != str:
    print('Error: Song not recognized or recording not found')
else:
    CHORDS_LINK = ChordFind.chordFind(SONG_DETAILS)
    TABS_LINK = SongsterrFind.songsterrFind(SONG_DETAILS)

def finalForm():
    if CHORDS_LINK == '' and TABS_LINK == '':
        print('No chords or tabs could be found!')
    elif CHORDS_LINK == '':
        FORM = input("Only tabs were found. Type 'TABS' to see them: ")
    elif TABS_LINK == '':
        FORM = input("Only chords were found. Type 'CHORDS' to see them: ")
    else:
        FORM = input("Chords and tabs were found. Type 'CHORDS' to see chords, 'TABS' to see tabs: ")

def retrieve():
        finalForm()

        if FORM.lower() == 'chords':
            final = CHORDS_LINK
        elif FORM.lower() == 'tabs':
            final = TABS_LINK
        else:
            print('Could not recognize input, try again')
            finalForm()
            if FORM.lower() == 'chords':
                final = CHORDS_LINK
            elif FORM.lower() == 'tabs':
                final = TABS_LINK
            else:
                print('Could not recognize input')

retrieve()



