import pygame
from random import randint

W = 600
H = 800
k = 1
x, y = 0, 0
STEP = 10
FPS = 30
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
a = randint(0, 600)
b = randint(0 , 800)
score = 0
font = pygame.font.SysFont('verdana', 32)
text = font.render(str(score), True, BLUE) 
textRect = text.get_rect()  
textRect.center = (W - 50, 50)

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
    def update(self):
        if self.rect.x < 460:
            self.rect.x += x + k * a
        #if self.rect.x > 0:
         #   self.rect.x -= x + k * a
#

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
    pygame.time.delay(20)     
    pygame.display.update()            