#import pygame
#pygame.mixer.init()
#pygame.mixer.music.load("otter_happy.wav")
#pygame.mixer.music.play()


import os

def happy_noise():
    os.system('mpg321 happy_otters.mp3 &')

def angry_noise():
    os.system('mpg321 otter_sounds/otter_angry.mp3 &')

def normal_noise():
    os.system('mpg321 otter_sounds/otter_normal.mp3 &')


happy_noise()
