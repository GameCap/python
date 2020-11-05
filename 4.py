import pygame
pygame.init()
surface = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Figures")
BLUE = (0, 204, 255)
class Figure():
    def __init__(self, perimeter=None, space=None):
        self.perimeter = perimeter
        self.space = space
        self.infoFig = []
    def calcPerimeter(self):
        pass
    def calcSpace(srlf):
        pass
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('периметр = %s площадь = %s' %(p, s))
class Rectangle(Figure):
    def __init__(self, x, y, w, h):
        Figure.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def calcPerimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter
    def calcSpace(self):
        space = self.x * self.y
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('Имя=прямоугольник, периметр = %s площадь = %s' %(p, s))
class Square(Figure):
    def __init__(self, w):
        Figure.__init__(self)
        self.w = w
    def calcPerimeter(self):
        perimeter = self.w * 4
        return perimeter
    def calcSpace(self):
        space = self.w * self.w
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('Имя=квадрат, периметр = %s площадь = %s' %(p, s))
class Circle(Figure):
    def __init__(self, r, p):
        Figure.__init__(self)
        self.r = r
        self.p = p
    def calcPerimeter(self):
        perimeter = self.r * 2 * self.p
        return perimeter
    def calcSpace(self):
        space = self.r * self.r * self.p
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('Имя=круг, периметр = %s площадь = %s' %(p, s))
class Trapezoid(Figure):
    def __init__(self, a, b, h, c):
        Figure.__init__(self)
        self.a = a
        self.b = b
        self.h = h
        self.c = c
    def calcPerimeter(self):
        perimeter = self.a + self.b + self.c + self.c 
        return perimeter
    def calcSpace(self):
        space = self.a / 2 + self.b / 2 * self.h
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('Имя=трапеция, периметр = %s площадь = %s' %(p, s))
class Ellipse(Figure):
    def __init__(self, a, b, p):
        Figure.__init__(self)
        self.a = a
        self.b = b
        self.p = p
    def calcPerimeter(self):
        perimeter = 4 * (self.p * self.a * self.b + (self.a + self.b) * (self.a - self.b)) / (self.a + self.b)
        return perimeter
    def calcSpace(self):
        space = self.p * self.a * self.b
        return space
    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('Имя=Эллипс, периметр = %s площадь = %s' %(p, s))
if __name__ == '__main__':
    fig1 = Rectangle(5, 5, 10, 10)
    fig2 = Square(5)
    fig3 = Circle(3, 3.14)
    fig4 = Trapezoid(6.6, 9.2, 5.3, 7.3)
    fig5 = Ellipse(5, 10, 3.14)
    array = [fig1, fig2, fig3, fig4, fig5]
    for f in array:
        f.figInfo()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(surface, BLUE, (10, 10, 190, 380), 5)
    pygame.display.update()
    pygame.draw.rect(surface, BLUE, (200, 10, 190, 190), 5)
    pygame.display.update()
    pygame.draw.circle(surface, BLUE, (504, 124), 114, 5)
    pygame.display.update()
    pygame.draw.lines(surface, BLUE, True, [[650, 10], [900, 10], [950, 210], [600, 210]], 5)
    pygame.draw.ellipse(surface, BLUE, (200, 200, 190, 380), 7)
    pygame.display.update()
