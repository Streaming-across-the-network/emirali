import vlc

# creating vlc media player object
media = vlc.MediaPlayer("com.oculus.shellenv-20220525-222755.mp4")

# start playing video
media.play()

while True:
    pass
