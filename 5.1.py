import pygame
from random import randint
a = randint(0, 800)
b = randint(0, 600)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
x, y = a, b
r = 10
c = (x, y)
type = pygame.MOUSEMOTION
mouse_pos = pygame.mouse.get_pos()

W, H = 800, 600

sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)

while True:
    for i in pygame.event.get() :
        if i.type == pygame.QUIT:
            exit()
        if mouse_pos == c:
            x, y = a, b;
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, [x, y, r, r], 3)
    pygame.display.update()