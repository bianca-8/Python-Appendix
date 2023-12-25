from pygame import *

init()
screen = display.set_mode((400, 400))
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#dimensions of the red box
box_X = 100; box_Y = 50; box_W = 200; box_H = 100;
button = Rect(box_X, box_Y, box_W, box_H)

myFont = font.SysFont("Times New Roman",30)
text = myFont.render("PLAY" , 1, BLACK)

#get the width and height of the text
text_Width, text_Height = myFont.size("PLAY")

#find the x and y for the text to be centered
text_X = box_X + (box_W - text_Width)//2
text_Y = box_Y + (box_H - text_Height)//2

#assign the Rect of the text 
textRect = Rect(text_X, text_Y, text_Width, text_Height)


  
screen.fill(GREEN)
draw.rect(screen,RED,button)
screen.blit(text, textRect)

display.update()
time.wait(50000)
quit()
