import pygame
import os

_image_library = {} #you need ball.png in the same folder
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

speedx = 3
speedy = 3
lives = 4
x = 180
y = 120 #this x and y sets the "spawn point" of the ball in the middle of the screen
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    if lives != 0 : #ball can only move if it has more than 0 lives
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= speedy
        if pressed[pygame.K_DOWN]: y += speedy
        if pressed[pygame.K_LEFT]: x -= speedx
        if pressed[pygame.K_RIGHT]: x += speedx

        if x >= 360:
            x = x - 30
            lives = lives - 1
            print("lives: "+str(lives))
        if x <= 0:
            x = x + 30
            lives = lives - 1
            print("lives: "+str(lives))
        if y >= 260:
            y = y - 30
            lives = lives - 1
            print("lives: "+str(lives))
        if y <= 0:
            y = y + 30
            lives = lives - 1
            print("lives: "+str(lives)) # "bounce" effect sets ball back by a certain amount in the axis it violated

    
    else :
        print("no more lives loser")
        done = True #ends game
    
    screen.fill((255, 255, 255))

    screen.blit(get_image('ball.png'), (x, y))

    pygame.display.flip()
    clock.tick(60)
