# Lyrics-on-wheels

## Introduction
I was surfing YouTube one day and I came across a few lyrical videos of famous songs.

- [Sorry](https://www.youtube.com/watch?v=rBistsB7pNU)
- [Shape of You](https://www.youtube.com/watch?v=TRkIdcuXZQg)
- [Baby](https://www.youtube.com/watch?v=Uim4GwSfzxY)
- [Sugar](https://www.youtube.com/watch?v=48VSP-atSeI)
- [Love Yourself](https://www.youtube.com/watch?v=TMSIR210mRg)

**All these lyrical videos are unofficial, yet they have millions of views!!**

I was lazy and did not think I would enjoy creating lyrical videos manually (using tools like Premier Pro). So I felt I could automate this process of content creation and get millions of views as well. :wink:

I came across the [MoviePy](https://pypi.org/project/moviepy/) python library which is used to create, trim, and edit videos. Thanks to the amazingly talented [Zulko](https://github.com/Zulko) for creating the library.

## Built With

- `Python 3.5.2`
- `MoviePy 1.0.3`

## Getting Started

- [Install MoviePy](https://github.com/Zulko/moviepy#installation).
- Clone or download this repo.
- Generate lrc file from [LRCGenerator](https://lrcgenerator.com/).
- Keep your lrc file and song file in the location where `lyrics.py` is present.
- Change the lrc file name and song file name in `lyrics.py`.
- Open terminal/cmd to execute `python3 lyrics.py`.

If you are having any trouble, try again after installing the [optional dependencies](https://github.com/Zulko/moviepy#optional-but-useful-dependencies) as well.

**Note:** You might need to exceute `sudo python3 lyrics.py` (basically admin mode) based on your user permissions and system configuration because of the PyGame dependency.

## What can be improved

Initilay, I tried to extract lyrics directly from the song so that the song will be the only input for the script. After some basic research on lyric extraction models, I felt that the accuracy wasn't good enough which would enable complete automation. The amount of accuracy I could get did not balance the amount of complexity that is being added. 

So I used [LRCGenerator](https://lrcgenerator.com/), which is an amazing tool to create lrc files for any song. It only takes as much time as the duration time of your song.

**Note:** If you know of any DL models/classical programs which can extract lyrics from all types of songs, please feel free to contribute :)

## Contributing

If you have any issues, questions, or ideas to improve this, please feel free to open an issue on the [issues page](https://github.com/nvinayvarma189/Media-Automation-Python/issues) first and then open a Pull request.

1. Fork the project on GitHub.
2. Clone the forked project to your local system.
3. Create your feature branch (`git checkout -b feature/AmazingFeature`).
4. Add the change you made (`git add .`).
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
6. Push to the branch (`git push origin feature/AmazingFeature`).
7. Open a pull request from your forked repo.

## The reason I did not upload it to YT

When I was about to upload the generated video to YT, I came across copyright infringement rules for music videos. You can read about it from this [quora answer](https://www.quora.com/Can-I-make-money-from-lyrics-videos-on-YouTube) (also please read answers from other related questions as well).

Even though there are some tricks to avoid copyright infringement, after going through the quora answers, it did not feel right for me to upload something which is 90% someone else's work (music, lyrics, etc). Music producers get their music copyrighted for a reason. So I just refrained myslef from uploading. But this was still something fun to build. :)

In case you want to upload such content online, please make sure you understnad the potential complications as well. Cheers!!
