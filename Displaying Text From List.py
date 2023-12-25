from pygame import *
init()
screen = display.set_mode((400, 400))

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

myFont = font.SysFont("Times New Roman",20)

myList = ["White","Oaks","Secondary","School"]

running = True

while running:
  
  text_X = 50
  text_Y = 50

  screen.fill(GREEN)
  
  for e in event.get():  # get all the events
    if e.type == QUIT:
      running = False
        
  for word in myList:
    text = myFont.render(word , 1, BLACK)
    screen.blit(text, (text_X,text_Y,200,100))
    text_Y += 20
      
  display.update()
    
quit()
