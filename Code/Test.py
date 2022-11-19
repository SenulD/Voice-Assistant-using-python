import vlc
import time
from favouritemusics import *

print("st")

for i in range(0,150):
    
    p = vlc.MediaPlayer(songs[i])
                                            #r"C:\Users\Senul\Music\Adele - Rolling in the Deep (Official Music Video).mp3"
    p.play()

    print('is_playing:', p.is_playing())    

    time.sleep(0.5)                          # sleep. it need some time to start 

    print('is_playing:', p.is_playing())    

    while p.is_playing():
        time.sleep(0.5)                        # sleep 

        


