import sys
import pygame
from random import randint
from pygame.locals import QUIT
from pygame.locals import Rect
pygame.init

width = 800
height = 600
balloon2 = Actor('balloon')
balloon2.pos = 400,300
bird = Actor('house')
house.pos = randint(800,1600),randint(10,200)

tree.pos = randint(800,1600),450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
scores = []

def update_high_scores():
    pass

def display_high_scores():
    pass