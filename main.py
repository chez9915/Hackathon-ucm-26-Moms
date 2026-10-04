"""
import pygame
import sys

#pygame setup
pygame.init()
#I don't know what these number mean fiddle with them and find out
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    #poll for events
    #pygame.quit event means the user clicked x to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #render game here

    #flip the display to your work on the screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
"""