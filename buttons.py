import pygame
from resources import W, H

pygame.init()

objects = []
f_sys = pygame.font.SysFont('tflextypea', 50)


class Button():
    def __init__(self, x, y, width, height, buttonText = "Button", onclickFunction = None, onePress = False ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onePress = onePress
        self.onclickFunction = onclickFunction

        self.colors = {"normal" : (220, 220, 220),
                       "hover" : (245, 227, 227),
                       "pressed" : (162, 156, 156)}

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        self.buttonTextSurf = f_sys.render(buttonText, 1, (0,0,0))

        objects.append(self)

    def process(self, screen):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.colors['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.colors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.colors['pressed'])
                if self.onePress:
                    self.onclickFunction()

        self.buttonSurface.blit(self.buttonTextSurf, [
            self.buttonRect.width / 2 - self.buttonTextSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonTextSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    print('Button Pressed')


