"""Edit text with the keyboard."""
import pygame
from pygame import *
#import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

init()
screen = display.set_mode((640, 240))

text = 'this text is editable'
font = font.SysFont('Arial', 25)
img = font.render(text, 1, RED)

rect = img.get_rect()
print(rect)
rect.topleft = (20, 20)


running = True
background = GRAY

while running:
    for e in event.get():      
        if e.type == QUIT:
            running = False
        
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += e.unicode
              
            img = font.render(text, 1, RED)
            rect.size=img.get_size()
           
    
    screen.fill(background)
    screen.blit(img, rect)
    draw.rect(screen,RED,rect,1)
    display.update()

quit()
