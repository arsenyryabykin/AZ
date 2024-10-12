import pygame.image
from pygame import display
import os

pygame.init()

info_object = display.Info()
W_ = info_object.current_w
H_ = info_object.current_h
#


W = 2560
H = 1440

# Цвета
WHITE = (255,255,255)
BLACK = (0, 0, 0)

radius = 50

axes = pygame.image.load('axes.png')

if not os.path.isdir("pics"):
    os.mkdir('pics')