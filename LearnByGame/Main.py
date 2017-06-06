# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Fofight Fong <Learnbgame>. All rights reserved.
#
# This file is part of LearnByGame.
#
#the "@0" means start and "@1" means end

import math
import sys
import pygame
import time
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN


#import my own modules
import keyboardrules
import chelement


SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600

pygame.init()
pygame.font.init()
pygame.mixer.init()


everything = pygame.sprite.Group()

#####energy form@0

TEMPERATURE = []#ABSOLUTEzERO~INIFINITE
'''the degree or intensity of heat present in a substance
or object, especially as expressed according to a
comparative scale and shown by a thermometer or perceived by touch'''

FORCE = []#
'''strength or energy as an attribute of physical action or movement'''

SOUND = []#
'''vibrations that travel through the air or another medium and
can be heard when they reach a person's or animal's ear.'''

LIGHT = []

#####energy form@1

ABSOLUTEzERO = "-273.15"#
'''the lowest temperature that is theoretically 
possible, at which the motion of particles that constitutes 
heat would be minimal. It is zero on the Kelvin scale, equivalent
to –273.15°C or –459.67°F'''

INIFINITE = "∞"

VITALITY = []#the proof of living creatures

SPEED = []

def death():
    if VITALITY = 0:
        #end of life
        pass
def heat():
    t = TEMPERATURE
    '''when the temperature reaches a certain range,the vitality 
of the creature disappears'''
    if T[]<t<t[]:
        VITALITY = 0
        death()
        pass



def time():
    pass

def chat():
    #langue,form,
    pass

def verification():
    #verify true or fault
    pass



def money():
    #load bitcoin's picture
    #take bitcoin as currency,
    #188.8->1+2+5
    pass

def annotate():
    #explain or annotations related content,
    pass

class Map:
    #draw the map
    pass

def task():
    pass

def equation():
    #guide the chemical reaction
    #
    pass

def prohibited():
    #we set the rules to prevent something from happening
    #something is forbited,but as we all know,nothing is absolutely forbited
    #as long as meet certain conditions,the rules can be broken
    pass















def main():
    game_over = False
    
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIFHT],DOUBLEBUF)
    pygame.display.set_caption('welcome to the LeanByGame!!!')
    background = pygame.image.load()
    clock = pygame.time.Clock()
    enemies = pygame.sprite.Group()
    hero = pygame.sprite.Group()
    while True:
        clock.tick(60)
        screen.blit(background,[0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if not game_over:
                if event.type == KEYDOWN:
                    keyboardrules.pygameKeyboardRule_KEYDOWN()
                    
                if event.type == KEYUP:
                    keyboardrules.pygameKeyboardRule_KEYUP()
                    
                 
                    
    
    #load background music
    #load the scene
       

#if __name__ == "__main__":
#    main()





















        
