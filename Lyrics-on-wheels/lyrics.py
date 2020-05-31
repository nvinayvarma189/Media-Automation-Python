import numpy as np
from moviepy.editor import AudioFileClip, ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips
from moviepy.video.tools.segmenting import findObjects
import datetime

def timeDiff(nxt, crnt):
    df = '%M:%S.%f'
    diff = datetime.datetime.strptime(nxt, df)\
    - datetime.datetime.strptime(crnt, df)
    microseconds = diff.microseconds
    seconds = diff.seconds
    return seconds + microseconds/1000000

songClip = AudioFileClip("./Dekhte_Dekhte.mp3") # extract audio clip
lrcFile = open('./Dekhte_Dekhte.lrc', 'r')
lines = lrcFile.readlines() # read the lyrics

bgImageClip = ImageClip('./img/background.jpg') # background image for the video

beginTimeStamp = '00:00.00'
firstLyricTimeStamp = lines[5][1:9]
songDuration = lines[-1][1:9]
screensize = (1920, 1080)
lastLineFlag = 0

fillerText = TextClip('Dekthe Dekthe',color='white', font="Amiri-Bold", kerning = 5, fontsize=100) # Text to dispaly before lyrics start
fillerDuration = timeDiff(firstLyricTimeStamp, beginTimeStamp) # time before lyrics start
fillerVideoClip = CompositeVideoClip( [bgImageClip.set_pos('center').set_duration(fillerDuration), fillerText.set_pos('center').set_duration(fillerDuration)], size=screensize) # video clip where filler text is displayed on background image
videoClips = [fillerVideoClip] # add the video clip to a list

for i in range(5, len(lines)): #start reading lyrics
    lyricStrip = lines[i][10:]
    currentLineTimeStamp = lines[i][:10][1:-1]
    print(currentLineTimeStamp)
    origLyric = lyricStrip.split('!!')[0].lstrip().rstrip() # lyric strip in original language
    engLyric = lyricStrip.split('!!')[1].lstrip().rstrip() # lyric strip in translated language
    disaplayText = origLyric+'\n'+'\n'+'*******************'+'\n'+engLyric # display text at each time step
    LyricClip = TextClip(disaplayText, color='white', font="Amiri-Bold", kerning = 5, fontsize=60) # text clip for combined lyrics
    if (lines[i+1] == '\n'):
        duration = timeDiff(songDuration, currentLineTimeStamp) # calculate time period to display lyric
        lastLineFlag = 1 # if last lyric is reached
    else:
        nextLineTimeStep = lines[i+1][:10][1:-1]
        duration = timeDiff (nextLineTimeStep, currentLineTimeStamp) # calculate time period to display lyric

    lyricVideoClip = CompositeVideoClip( [bgImageClip.set_pos('center').set_duration(duration), LyricClip.set_pos('center').set_duration(duration)], size=screensize) # create a video clip for each lyric step
    # lyricVideoClip = lyricVideoClip.on_color(size=None, color=(1, 1, 1), pos='center', col_opacity=1)
    videoClips.append(lyricVideoClip) # add video clips to list
    if (lastLineFlag):
        break

final_clip = concatenate_videoclips(videoClips)

final_clip = final_clip.set_audio(songClip)
final_clip.write_videofile('Dekhte_Dekhte_Lyrical.mp4',fps=25,codec='libx264')