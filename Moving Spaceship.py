# use arrows to move the spaceship

from pygame import * 
init()
size = width, height = 1000, 700
screen = display.set_mode(size)

RED = (255,0,0)

# movement key booleans
PRESS_RIGHT = False
PRESS_LEFT = False
PRESS_UP = False
PRESS_DOWN = False
SHOOT = False

# Load images
# Spaceship
shipPic = image.load("spaceship.png")
shipWidth = shipPic.get_width()//4
shipHeight = shipPic.get_height()//4
shipPic = transform.scale(shipPic, (shipWidth, shipHeight ))
#shipPic = transform.rotate(shipPic, 180)   # rotate image 180 degrees

# Background
spaceBackground = image.load("background.jpg")
spaceBackground = transform.scale(spaceBackground, (1000,700)) # resize the image


def drawScene(screen, shipx, shipy, bullet):
   
  screen.blit(spaceBackground,(0,0,1000,700))
  screen.blit(shipPic, (shipX,shipY,shipWidth,shipHeight))
  while bullet != []:
      for i in bullet:
        if i[1] > 0:
          i[1] -= 20
          draw.line(screen,RED,(i[0]+90,i[1]),(i[0]+90,i[1] - 10),2)
        else:
          bullet.remove(i)
        
    
      
    
running = True
myClock = time.Clock()

shipX = 0
shipY = 0
bullet = []
moveRate = 5

# Game Loop
while running:
    for e in event.get():             # checks all events that happen
      
        if e.type == QUIT:
            running = False
        
        elif e.type == KEYDOWN:
            if e.key == K_RIGHT:
                PRESS_RIGHT = True
            if e.key == K_LEFT:
                PRESS_LEFT = True 
            if e.key == K_UP:
                PRESS_UP = True
            if e.key == K_DOWN:
                PRESS_DOWN = True
            if e.key == K_SPACE:
                SHOOT = True
              
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                PRESS_RIGHT = False
            if e.key == K_LEFT:
                PRESS_LEFT = False 
            if e.key == K_UP:
                PRESS_UP = False
            if e.key == K_DOWN:
                PRESS_DOWN = False 
            if e.key == K_SPACE:
                SHOOT = False

    drawScene(screen, shipX, shipY, bullet)
    myClock.tick(60)                     # waits long enough to have 60 fps
    
    # for ship movement
    if PRESS_RIGHT == True:
        shipX += moveRate
    if PRESS_LEFT == True:
        shipX -= moveRate  
    if PRESS_UP == True:
        shipY -= moveRate
    if PRESS_DOWN == True:
        shipY += moveRate 
    if SHOOT == True:
      bullet.append([shipX,shipY])
    display.flip()


quit()
