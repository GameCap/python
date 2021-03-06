import pygame
from random import randrange

W = 600
H = 800
#j = randrange(-1, 1, 2)
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
textRect1.center = (W - 50, 50) 
text2 = font.render(str(score2), True, BLUE) 
textRect2 = text2.get_rect()  
textRect2.center = (50, 50) 

class Gate1(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (250, 0)
class Gate2(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (250, 775)


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
    
    def update(self):
        self.rect.x += g * self.dx
        self.rect.y += h * self.dy
        if self.rect.x > 540 or self.rect.x < 10:
            self.dx = -self.dx
        if self.rect.y > 740 or self.rect.y < 10 :
             self.dy = -self.dy

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

gate1 = Gate1(W//2, H//2, "gif/images.jpg")
gate2 = Gate2(W//2, H//2, "gif/images.jpg")
pl1 = Player1(W//2, H//2, "gif/z.png")
pl2 = Player2(W//2, H//2, "gif/z.png")
ball = Ball(W//2, H//2, "gif/ft.png") 
bg = Background(W//2, H//2, "gif/field.jpg")
clock = pygame.time.Clock()

if __name__ == '__main__':
    counter = 0
while True:
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

    
    if pygame.sprite.collide_rect(ball, gate1):
            score1 += 1
            ball.rect.center = (300, 400)
            pygame.time.wait(1000)             
    if pygame.sprite.collide_rect(ball, gate2):
            score2 += 1
            ball.rect.center = (300, 400)
            pygame.time.wait(1000) 

    if pygame.sprite.collide_rect(ball, pl1):   
        if ball.rect.x - 25 and ball.rect.x + 25 < pl1.rect.x and (pl1.rect.y +50):
            ball.dx = ball.dx
            ball.dy = -ball.dy
        if ball.rect.x - 25 and ball.rect.x + 25> pl1.rect.x and (pl1.rect.y +50):
            ball.dx = -ball.dx
            ball.dy = -ball.dy 
    if pygame.sprite.collide_rect(ball, pl2):
        if ball.rect.x - 25 and ball.rect.x + 25 > (pl2.rect.x and pl2.rect.y - 50):
            ball.dx = ball.dx
            ball.dy = -ball.dy
        if ball.rect.x - 25 and ball.rect.x + 25 < (pl2.rect.x and pl2.rect.y - 50):
            ball.dx = -ball.dx
            ball.dy = -ball.dy  
     
    surface.fill(BLACK)
    surface.blit(bg.image, bg.rect)
    bg.update()
    gate1.update()
    gate2.update()
    text1 = font.render(str(score1), True, BLUE)
    surface.blit(text1, textRect1)
    text2 = font.render(str(score2), True, BLUE)
    surface.blit(text2, textRect2)
    surface.blit(pl1.image, pl1.rect)
    pl1.update()        
    surface.blit(pl2.image, pl2.rect)        
    pl2.update()
    surface.blit(ball.image, ball.rect)
    ball.update()    
    pygame.display.update()
    pygame.time.delay(50) 

    if score1 == 2:
        tx = font.render("Player 2 win",True,BLACK)
        surface.blit(tx, [200,400])
        ball.kill()
        ball.update()
        pl1.kill()
        pl2.kill()
        pygame.display.update()
        pygame.time.delay(50)
        
    if score2 == 2:
        tx = font.render("Player 1 win",True,BLACK)
        surface.blit(tx, [200,400])
        ball.kill()
        pl1.kill()
        pl2.kill()           
        pygame.display.update()
        pygame.time.delay(50)            