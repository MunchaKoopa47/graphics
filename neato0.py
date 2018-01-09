# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (150, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREEN = (0, 125, 0)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GRAY = (76, 76, 76)
BROWN = (51, 19, 0)
    
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(400, 600)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)
        
# Game loop
done = False


def draw_landscape():
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

def draw_house():
    pygame.draw.rect(screen, RED, [200, 210, 200, 200])
    pygame.draw.polygon(screen, BROWN, [[ 190, 210], [410,210], [300, 100]])
    pygame.draw.rect(screen, BROWN, [240, 300, 60, 110])

def draw_sky():
    screen.fill(BLACK)

def draw_moon(x, y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])
    pygame.draw.rect(screen, BLACK, [x, y + 50, 100, 20])
    pygame.draw.rect(screen, BLACK, [x + 20, y, 20, 100])


def draw_fence():
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

def draw_stars():
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

def make_grass():
    stars = []
    for i in range(10):
        x = random.randrange(0, 800)
        y = random.randrange(0, 400)
        r = random.randrange(1, 5)
        s = [x, y, r, r]
        stars.append(s)

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [x, y, 20, 100])








while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw
    draw_sky()
    draw_moon(575, 75)
    draw_stars()
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)
    draw_landscape()
    draw_tree(600, 300)
    draw_house()
    draw_fence()

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
