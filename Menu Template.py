# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

from pygame import * 
init()
size = width, height = 400, 400
screen = display.set_mode(size)

#define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# define fonts
menuFont = font.SysFont("Times New Roman",20)

#states in the Game
STATE_MENU = 0
STATE_GAME = 1
STATE_HELP = 2
STATE_QUIT = 3

def drawMenu(screen, button, mx, my, state):
    blockWidth = width//3
    blockHeight = height//7    
    rectList = [Rect(blockWidth, blockHeight, blockWidth, blockHeight), # game choice
                Rect(blockWidth, 3*blockHeight, blockWidth, blockHeight), #help choice
                Rect(blockWidth, 5*blockHeight, blockWidth, blockHeight)] # quite choice
    stateList = [STATE_GAME, STATE_HELP, STATE_QUIT]
    titleList = ["Play Game", "Help", "Quit Game"]
    draw.rect(screen, RED, (0, 0, width, height))
    
    for i in range(len(rectList)):
        rect = rectList[i] # get the current Rect
        draw.rect(screen, GREEN, rect)  # draw the Rect
        text = menuFont.render(titleList[i] , 1, BLACK)	# make the font
        textWidth, textHeight = menuFont.size(titleList[i]) # get the font size
        useW = (blockWidth - textWidth)//2  #use for centering
        useH = (blockHeight - textHeight)//2
        # getting a centered Rectangle
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)	# draw to screen
        
        if rect.collidepoint(mx, my):
            draw.rect(screen, BLACK, rect, 2)
            if button == 1:
                state = stateList[i]
    return state

    
def drawGame(screen, button, mx, my, state):
    draw.rect(screen, BLUE, (0, 0, width, height))
    if button == 3:
        state = STATE_MENU
    return state
    
def drawHelp(screen, button, mx, my, state):
    draw.rect(screen, GREEN, (0, 0, width, height))
    if button == 3:
        state = STATE_MENU
    return state

running = True
myClock = time.Clock()
# initializing variables
state = STATE_MENU
mx = my = 0

# Game Loop
while running:
    button = 0
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos          
            button = e.button
        elif e.type == MOUSEMOTION:
            mx, my = e.pos          
            #button = e.button 
            
    if state == STATE_MENU:                
        state = drawMenu(screen, button, mx, my, state)
    elif state == STATE_GAME:
        state = drawGame(screen, button, mx, my, state)
    elif state == STATE_HELP:
        state = drawHelp(screen, button, mx, my, state)
    else:
        running = False
        
    display.flip()
    myClock.tick(60)                     # waits long enough to have 60 fps
    
quit()
