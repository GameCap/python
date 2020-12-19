import pygame
from random import randint

W = 600
H = 800
#j = -1
x, y = 0, 0
STEP = 10
FPS = 20
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
g = 10
h = 10

score1 = 0
score2 = 0

pygame.init()
surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Football")

font = pygame.font.SysFont('verdana', 32)
text1 = font.render(str(score1), True, BLUE) 
textRect1 = text1.get_rect()  
textRect1.center = (50, 50) 
text2 = font.render(str(score2), True, BLUE) 
textRect2 = text2.get_rect()  
textRect2.center = (W - 50, 50) 

class Gate1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gif/images.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
class Gate2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gif/images.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


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
        self.dx = 1
        self.dy = 1
    
    #Тут он начинает лететь в рандомную сторону но после тго как доходит до границы по х 
    #он начинает опускать вниз доходит до корая у и всё. Подскажите что делать пожалуйста.
    def update(self):
        self.rect.x += g * self.dx
        self.rect.y += h * self.dy
        if self.rect.x > 540 or self.rect.x < 10:
            self.dx = -self.dx
        if self.rect.y > 740 or self.rect.y < 10 :
             self.dy = -self.dy
        
            
                  
            
        #if self.rect.y > 700 or self.rect.y < 75:
            #self.rect.y += j * h

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

gate1 = pygame.sprite.Group() 
gate1.add(Gate1(250, 0))
gate2 = pygame.sprite.Group() 
gate2.add(Gate2(250, 750))
pl1 = Player1(W//2, H//2, "gif/z.png")
pl2 = Player2(W//2, H//2, "gif/z.png")
ball = Ball(W//2, H//2, "gif/ft.png") 
bg = Background(W//2, H//2, "gif/field.jpg")
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

    
    if pygame.sprite.spritecollideany(ball, gate1):
            score1 += 1
            ball.rect.center = (300, 400)            
    if pygame.sprite.spritecollideany(ball, gate2):
            score2 += 1
            ball.rect.center = (300, 400)

    if pygame.sprite.spritecollideany(ball, pl1):
           ball.dx = -ball.dx

    for i in gate1:
            surface.blit(i.image, i.rect)
    for i in gate2:
            surface.blit(i.image, i.rect)
     
    surface.fill(BLACK)
    surface.blit(bg.image, bg.rect)
    bg.update()
    gate1.update()
    gate2.update()
    text1 = font.render(str(score1//2), True, BLUE)
    surface.blit(text1, textRect1)
    text2 = font.render(str(score2//2), True, BLUE)
    surface.blit(text2, textRect2)
    surface.blit(pl1.image, pl1.rect)
    pl1.update()        
    surface.blit(pl2.image, pl2.rect)        
    pl2.update()
    surface.blit(ball.image, ball.rect)
    ball.update()    
    pygame.display.update()
    pygame.time.delay(150)             