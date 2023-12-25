# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

from pygame import * 
init()
size = width, height = 400, 400
screen = display.set_mode(size)

myClock = time.Clock()

#define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# define the Rect for the green rectangle
boxX = 100
boxY = 100
boxWidth = 200
boxHeight = 100
rect = Rect(boxX,boxY,boxWidth,boxHeight)

# define fonts
myFont = font.SysFont("Times New Roman",60)
myFont2 = font.SysFont("Verdana",20)

# make the font
text = myFont.render("Play" , 1, BLACK)
text2 = myFont2.render("The game is starting...",1,BLUE)

# get the font size    
textWidth, textHeight = myFont.size("Play") 

textX = (boxWidth - textWidth)//2  #use for centering
textY = (boxHeight - textHeight)//2
# getting a centered Rectangle
textRect = Rect(textX+boxX, textY+boxY, textWidth, textHeight)

# mouseX and mouseY
mx = 0
my = 0

running = True
# Game Loop
while running:
  
  button = 0
  
  for e in event.get():   
    if e.type == MOUSEBUTTONDOWN:
      mx, my = e.pos          
      button = e.button
    elif e.type == MOUSEMOTION:
      mx, my = e.pos          


    screen.fill(RED)
    # draw the Rect
    draw.rect(screen, GREEN, rect) 
    # draw the text
    screen.blit(text, textRect)	
    # check for collision and draw the black outline   
    if rect.collidepoint(mx, my):
      draw.rect(screen, BLACK, rect, 2)
      
      if button == 1:
        draw.rect(screen, BLUE, rect)
        screen.blit(text, textRect)
        screen.blit(text2,(100,250))
        
  display.flip()
  myClock.tick(60)
    
quit()
