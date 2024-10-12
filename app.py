import sys
import pygame
from resources import W, H, W_, H_
from resources import WHITE
from func import make_cartogram, make_case, anim
from common import save, menu

pygame.key.set_repeat(0)

class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED)

        self.clock = pygame.time.Clock()

        self.AppStateManager = AppStateManager('start')

        self.start = Start(self.screen, self.AppStateManager)
        self.wb_cartogram = WB_cartogram(self.screen, self.AppStateManager)
        self.color_cartogram = Color_cartogram(self.screen, self.AppStateManager)
        self.case_1 = Case(self.screen, self.AppStateManager, 1)
        self.case_2 = Case(self.screen, self.AppStateManager, 2)
        self.case_3 = Case(self.screen, self.AppStateManager, 3)
        self.case_4 = Case(self.screen, self.AppStateManager, 4)
        self.case_5 = Case(self.screen, self.AppStateManager, 5)
        self.case_6 = Case(self.screen, self.AppStateManager, 6)
        self.animation = Animation(self.screen, self.AppStateManager)


        self.states = {'start': self.start,
                       'wb_cartogram': self.wb_cartogram,
                       'color_cartogram': self.color_cartogram,
                       'case_1': self.case_1,
                       'case_2': self.case_2,
                       'case_3': self.case_3,
                       'case_4': self.case_4,
                       'case_5': self.case_5,
                       'case_6': self.case_6,
                       'animation': self.animation}

    def run(self):
        print("App running")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()

            self.states[self.AppStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(30)

class Start:
    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager

    def run(self):
        self.display.fill(WHITE)
        self.display.blit(menu(), (W / 2, H / 2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.AppStateManager.set_state('case_1')
        if keys[pygame.K_2]:
            self.AppStateManager.set_state('case_2')
        if keys[pygame.K_3]:
            self.AppStateManager.set_state('case_3')
        if keys[pygame.K_4]:
            self.AppStateManager.set_state('case_4')
        if keys[pygame.K_5]:
            self.AppStateManager.set_state('case_5')
        if keys[pygame.K_6]:
            self.AppStateManager.set_state('case_6')

        if keys[pygame.K_8]:
            self.AppStateManager.set_state('wb_cartogram')
        if keys[pygame.K_9]:
            self.AppStateManager.set_state('color_cartogram')
        if keys[pygame.K_0]:
            self.display.fill(WHITE)
            self.AppStateManager.set_state('animation')

class WB_cartogram:
    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager

        # self.tmp_surf = pygame.Surface((W, H))

    def run(self):

        make_cartogram(self.display, 'wb')

        # self.tmp_surf.fill(WHITE)
        # make_cartogram(self.tmp_surf, 'wb')
        # frame = pygame.transform.smoothscale(self.tmp_surf, (W_, H_))
        # self.display.blit(frame, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.AppStateManager.set_state('start')
        if keys[pygame.K_s]:
            save(self.display, "pics/WB_cartogram.png")
            print("сохранение WB_cartogram")

class Color_cartogram:
    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager

    def run(self):
        make_cartogram(self.display, 'colored')

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.AppStateManager.set_state('start')
        if keys[pygame.K_s]:
            save(self.display, "pics/Color_cartogram.png")
            print("сохранение Color_cartogram")

class Case:
    def __init__(self, display, AppStateManager, case_number):
        self.display = display
        self.AppStateManager = AppStateManager
        self.case_number = case_number

    def run(self):
        self.display.fill(WHITE)
        make_case(self.display, self.case_number)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.AppStateManager.set_state('start')
        if keys[pygame.K_s]:
            save(self.display, "pics/Case_" + str(self.case_number) + ".png")
            print("сохранение Case_" + str(self.case_number))

class Animation():

    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager
        self.m = 0

    def run(self):
        isRunning = 1
        while isRunning:
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()
                    if(event.key == pygame.K_ESCAPE):
                        self.AppStateManager.set_state('start')
                        self.m = 0
                        isRunning = False
                    if(event.key == pygame.K_LEFT):
                        if self.m != 0:
                            self.m -= 1
                        else:
                            continue
                        anim(self.display, self.m)
                        isRunning = False
                    if(event.key == pygame.K_RIGHT):
                        if self.m != 163:
                            self.m += 1
                        else:
                            continue

                        anim(self.display, self.m)
                        isRunning = False



class AppStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


if __name__ == '__main__':
    app = App()
    app.run()




