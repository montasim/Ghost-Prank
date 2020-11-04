#   Created on 11/04/2020
#   Created by Montasim


#   imporing pygame for display
import pygame

#   importing time for adjust timing of music and media
from time import sleep

#   staring pygame module
pygame.init()

#   defining display size. here fullscreen for any device
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#   initalizing music module
pygame.mixer.init()

#   loading background sound from file
pygame.mixer.music.load('media/sounds/ratsasan.mp3')

#   playing background sound
pygame.mixer.music.play()

#   pausing system for 5 sec
sleep(5)

#   loading background sound from file
pygame.mixer.music.load('media/sounds/scary.mp3')

#   playing background sound
pygame.mixer.music.play()

#   pausing system for 1 sec
sleep(1)

#   loading ghost image from file
image = pygame.image.load('media/image/scr.jpg')

#   set image to fullscreen
window.blit(image, (0,0))

#   showing ghost image
pygame.display.update()

#   pausing system for 3 sec for displaying image
sleep(3)