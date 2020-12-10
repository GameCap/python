import pygame
from random import randint

W = 600
H = 800
x, y = 0, 0
STEP = 10
SPEED = 2
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
a = randint(0, 600)
b = randint(0 , 800)

pygame.init()
surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Football")

class Player1 (pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 100)

    def moveLeft(self):
        self.rect.x -= STEP
    
    def moveRight(self):
        self.rect.x += STEP

class Player2 (pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        #self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 700)

    def moveLeft(self):
        self.rect.x -= STEP
    
    def moveRight(self):
        self.rect.x += STEP


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        #self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)


pl1 = Player1(W//2, H//2, "images/z.png")
pl2 = Player2(W//2, H//2, "images/z.png")
ball = Ball(W//2, H//2, "images/ft.png") 
bg = Background(W//2, H//2, "images/field.jpg")


while True:
    for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_RIGHT]:
        pl2.moveRight()
    elif keys[pygame.K_LEFT]:
        pl2.moveLeft()

    if keys[pygame.K_2]:
        pl1.moveRight()
    elif keys[pygame.K_1]:
        pl1.moveLeft() 
 

    surface.fill(BLACK)
    surface.blit(bg.image, bg.rect)
    bg.update()
    surface.blit(pl1.image, pl1.rect)
    pl1.update()        
    surface.blit(pl2.image, pl2.rect)        
    pl2.update()
    surface.blit(ball.image, ball.rect)
    ball.update()
    pygame.time.delay(20)     
    pygame.display.update()            