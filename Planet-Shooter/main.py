import random

import pygame
from pygame import mixer

# initialize game
pygame.init()
screen = pygame.display.set_mode((800, 600))

# title, logo and background
background = pygame.image.load('./assets/back.jpg')
icon = pygame.image.load('./planets/urenus.png')
pygame.display.set_caption('Planet Shooter')
pygame.display.set_icon(icon)


# score and over
score_value = 0
font = pygame.font.Font('./assets/firasans.otf', 20)
over = pygame.font.Font('./assets/firasans.otf', 56)


# space craft
craft = pygame.image.load('./assets/craft.png')
cord_move = 0
cordX = 368
cordY = 500


# bullet weapon
bullet = pygame.image.load('./assets/bullet.png')
bullY = cordY + 32 - 8
bull_fired = False
bull_move = 0.8
bullX = cordX


# planet photos
planetA = pygame.image.load('./planets/saturn.png')
planetB = pygame.image.load('./planets/earth.png')
planetC = pygame.image.load('./planets/jupiter.png')
planetD = pygame.image.load('./planets/neptune.png')
planetE = pygame.image.load('./planets/mars.png')
planetF = pygame.image.load('./planets/urenus.png')
planets = [planetA, planetB, planetC, planetD, planetE, planetF]
planet = planets[random.randint(0, 5)]
planX = random.randint(6, 730)
plan_move = 0.3
planY = -200


# functions
def showscore(): 
    score = font.render(f"score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

def spacecraft(x, y):
    screen.blit(craft, (x, y))

def planetS(x, y):
    screen.blit(planet, (x, y))

def throw_bull(x, y):
    global bull_fired
    bull_fired = True
    screen.blit(bullet, (x + 32 - 8, y))

def planet_hit(px, py, bx, by):
    if by <= py+64 and bx >= px-32 and bx <= px+32: return True
    else: return False

def craft_collision(px, py, cx):
    if py > 440 and cx+64 >= px and cx <= px+64: return True
    else: return False

def gameover():
    finished = over.render("GAME OVER", True, (255, 255, 255))
    credit = font.render("Masfik Alam", True, (255, 255, 255))
    screen.blit(finished, (270, 250))
    screen.blit(credit, (350, 330))


# game loop
running = True
while running:
    for event in pygame.event.get():
        # window quit
        if event.type == pygame.QUIT:
            running = False

        # craft movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cord_move += 0.5
            elif event.key == pygame.K_LEFT:
                cord_move -= 0.5
            elif event.key == pygame.K_SPACE:
                if not bull_fired: 
                    bullX = cordX
                    throw_bull(bullX, bullY)
                    sound = mixer.Sound('./assets/laser.wav')
                    sound.play()

        # release key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                cord_move = 0


    # screen color
    screen.fill((9,12,15))
    screen.blit(background, (0, 0))


    # trow bullet
    if bullY < 0: 
        bull_fired = False
        bullY = cordY + 32 - 8

    if bull_fired: 
        bullY -= bull_move
        throw_bull(bullX, bullY)

    
    # draw the craft
    cordX += cord_move
    if cordX < 6 : cordX = 6
    if cordX > 730: cordX = 730
    spacecraft(cordX, cordY)


    # draw the planet
    planY += plan_move
    if planY > 600:
        planY = -200
        planX = random.randint(6, 730)
    planetS(planX, planY)


    # hit planet with bullet
    if planet_hit(planX, planY, bullX, bullY):
        planY = -100
        score_value += 5
        plan_move += 0.01
        bull_fired = False
        bullY = cordY + 32 - 8
        planX = random.randint(6, 730)
        planet = planets[random.randint(0, 5)]

    
    # planet, craft collision
    if craft_collision(planX, planY, cordX):
        plan_move = 0
        cord_move = 0
        bull_move = 0
        gameover()


    # screen update
    showscore()
    pygame.display.update()
