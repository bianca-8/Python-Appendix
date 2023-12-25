from pygame import * 
init()
size = width, height = 300, 300
screen = display.set_mode(size)
button = 0
RED = (255,0,0)
BLACK = (0, 0, 0)
WHITE= (255, 255, 255)

color = RED
x = 20
y = 20
w = 100
h = 200

running = True
myClock = time.Clock()

# Game Loop
while running:
    for e in event.get():# checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos          
            button = e.button
            # left click button = 1, right click button = 3
            if button == 1 and mx > 20 and mx < 120 and my > 20 and my < 220:
                color = WHITE
            if button == 3 and mx > 20 and mx < 120 and my > 20 and my < 220:
                color = RED
                   
    draw.rect(screen,color, (x,y,w,h))
    
    display.flip()
    myClock.tick(60)                     # waits long enough to have 60 fps
    
quit()
