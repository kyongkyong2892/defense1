import sys
import pygame

import variables as var
import load 

import title
import menu

def display():
    var.screen.fill((255, 255, 255))
    pygame.display.flip()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            temp = pygame.mouse.get_pos()
            var.Mouse.lx = temp[0]
            var.Mouse.ly = temp[1]

            print(var.Mouse.lx, var.Mouse.ly)

def init():
    pygame.init()

    var.screen = pygame.display.set_mode((1024, 576))
    pygame.display.set_caption('Defense')

    load.data_load()

init()

while 1:
    display()
    input_handle()
