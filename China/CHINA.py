from just_playback import Playback
from threading import Thread
import time
import sys
import cv2


def music():
    playback = Playback()
    playback.load_file("Red_sun_in_the_sky.mp3")

    playback.play()
    playback.seek(5)

    time.sleep(10)
    playback.stop()


def image():

    img = cv2.imread("social_points.jpg", cv2.IMREAD_ANYCOLOR)

    while True:
        cv2.imshow("social_points.jpg", img)
        cv2.waitKey(0)
        sys.exit()  # to exit from all the processes


Thread(target=image).start()
Thread(target=music).start()
