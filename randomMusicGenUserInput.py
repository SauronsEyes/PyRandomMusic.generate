import pygame.midi,pygame
import time
import random
import threading


transpose = 0

instrumentInfo = []
numberOfInstruments = int(input("Enter number of Instruments: "))
for i in range(0,numberOfInstruments):
    print("Check the Following Link for MIDI Instrument: https://en.wikipedia.org/wiki/General_MIDI")
    mtype = input("Enter Midi Instrument Type for Instument "+str(i+1)+":")
    print("Check Notes ID for MIDI: https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies")
    mSNote = input("Enter Starting Note for the MIDI Instrument "+str(i+1)+":")
    mENote = input("Enter Ending Note for the MIDI Instrument "+str(i+1)+":")
    instrumentInfo.append({
                'startingNote':int(mSNote),
                'endingNote':int(mENote),
                'instrumentMidiID': int(mtype)
        })
    
notes = []
allNotes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
noteIdenitfier = []

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(25)

for i in range(0,128):
    noteIdenitfier.append(allNotes[i%len(allNotes)])
print(noteIdenitfier[24])


def generateNotes(initialNote,finalNote):
    tempGenNotes = []
    absNotePos = 1
    while(initialNote<finalNote):
        print(noteIdenitfier[initialNote],end=" ")
        tempGenNotes.append(initialNote)
        if(absNotePos == 3 or absNotePos == 7):
            initialNote = initialNote + 1
        else:
            initialNote = initialNote + 2
    
        
        absNotePos = absNotePos + 1
        if absNotePos>7:
            absNotePos = 1
    return tempGenNotes

for i in range(0,numberOfInstruments):
    notes.append(generateNotes(instrumentInfo[i]['startingNote'],instrumentInfo[i]['endingNote']))

print (notes)

def playRandomNotes(instrumentID):
    global player,notes
    player.set_instrument(instrumentInfo[instrumentID]['instrumentMidiID'])
    randomNote = random.randint(0, len(notes[instrumentID])-1)
    randomTime = 0.25;
    print(noteIdenitfier[notes[instrumentID][randomNote]],end='')
    randVel = random.randint(100, 127)
    player.note_on(notes[instrumentID][randomNote]+transpose, randVel)
    time.sleep(randomTime)
    player.note_off(notes[instrumentID][randomNote]+transpose, randVel)
    
openGenerator = True
while(openGenerator):
    for i in range(0,numberOfInstruments):
        threading.Thread(target=playRandomNotes,args=(i,)).start()
        time.sleep(0.125)
        print(',',end="")
    
    print("")
    
    
    
                
            

del player
pygame.midi.quit()
    



