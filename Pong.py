import pygame, sys
from pygame.locals import *
from Paddle import *
from Ball import *
from random import randint

#Start Pygame
pygame.init()

#Variables
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 720
FRAMERATE = 60
score = [0,0]

#Create screen, clock, and name window.
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()

# Create the Paddles(x,y,length,width,speed,playernumber).
paddle2 = Paddle(20, 10, 100, 20, 10, 2)
paddle1 = Paddle(740, 10, 100, 20, 10, 1)

# Spawn the Ball(x, y, xspeed, yspeed, size).
randomx = randint(2,3)
randomy = randint(3,5)
if(randint(0,100) > 50):
    randomx = -randomx
if(randint(0,600) > 300):
    randomy = -randomy
pongball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, randomx, randomy, 20)

# Draw a padle on the screen.
def drawPaddle(x, y, length, width):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,length,width))

# Draw the ball on the screen.
def drawBall(x, y, size):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,size,size))

# Used to create a random number for speed of ball.
def randomNumber(a,b):
    rand = randint(a,b)
    if(randint(1,2) == 1):
        rand = -rand
    return rand

# Determine if a point has been scored, and reset the ball location and speed.
def checkPoint(x):
    if(x < 0):
        score[1] += 1
        pongball.xpos = SCREEN_WIDTH/2
        pongball.ypos = SCREEN_HEIGHT/2
        pongball.xspeed = randomNumber(2,3)
        pongball.yspeed = randomNumber(3,5)
        pongball.pause = 2 * FRAMERATE
    elif(x > 760):
        score[0] += 1
        pongball.xpos = SCREEN_WIDTH/2
        pongball.ypos = SCREEN_HEIGHT/2
        pongball.xspeed = randomNumber(2,3)
        pongball.yspeed = randomNumber(3,5)
        pongball.pause = 2 * FRAMERATE


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Checking Variables
    k = pygame.key.get_pressed()
    paddle1.move(paddle1.ypos, k, paddle1.number)
    paddle2.move(paddle2.ypos, k, paddle2.number)
    pongball.move(pongball.xpos, pongball.ypos, pongball.xspeed, pongball.yspeed, paddle2, paddle1)
    
    # Drawing screen
    DISPLAYSURF.fill((0,0,0))
    
    
    # Draw ball and paddles
    drawBall(pongball.xpos, pongball.ypos, pongball.size)
    drawPaddle(paddle1.xpos, paddle1.ypos, paddle1.width, paddle1.length)
    drawPaddle(paddle2.xpos, paddle2.ypos, paddle2.width, paddle2.length)

    # Check for a point
    checkPoint(pongball.xpos)

    # Update display and tick clock.
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FRAMERATE)
