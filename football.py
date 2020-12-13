import pygame
from random import randint

W = 600
H = 800
j = -1
x, y = 0, 0
STEP = 10
FPS = 20
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
g = randint(-30, 30)
h = randint(-30, 30)

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
        if self.rect.x > 0:
            self.rect.x -= STEP
    
    def moveRight(self):
        if self.rect.x < 550:
            self.rect.x += STEP

class Player2 (pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        #self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 700)

    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= STEP
    
    def moveRight(self):
        if self.rect.x < 550:
            self.rect.x += STEP


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        #self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
    
    #Тут он начинает лететь в рандомную сторону но после тго как доходит до границы по х 
    #он начинает опускать вниз доходит до корая у и всё. Подскажите что делать пожалуйста.
    def update(self):
        self.rect.x += g
        self.rect.y += h
        if self.rect.x > 550 or  self.rect.x < 50:
            self.rect.x += j * g
        if self.rect.y > 750 or self.rect.y < 50:
            self.rect.y += j * h

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
clock = pygame.time.Clock()
if __name__ == '__main__':
    counter = 0
while True:
    counter += 1
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        clock.tick(FPS)
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
    pygame.display.update()
    pygame.time.delay(150)             