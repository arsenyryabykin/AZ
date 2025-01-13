import sys
import pygame
from config import W, H
from config import WHITE, BLACK
#from func import make_cartogram, make_case, anim
from make_cartogram import make_cartogram
from make_case import make_case, make_case_outline
from common import save, menu
from func import anim
import os
pygame.key.set_repeat(0)

class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED)

        self.clock = pygame.time.Clock()

        self.AppStateManager = AppStateManager('animation')
        # self.AppStateManager = AppStateManager('wb_cartogram')
        #
        # self.start = Start(self.screen, self.AppStateManager)
        # self.wb_cartogram = WB_cartogram(self.screen, self.AppStateManager)
        # self.color_cartogram = Color_cartogram(self.screen, self.AppStateManager)
        # self.case_1 = Case(self.screen, self.AppStateManager, 1)
        # self.case_2 = Case(self.screen, self.AppStateManager, 2)
        # self.case_3 = Case(self.screen, self.AppStateManager, 3)
        # self.case_4 = Case(self.screen, self.AppStateManager, 4)
        # self.case_5 = Case(self.screen, self.AppStateManager, 5)
        # self.case_6 = Case(self.screen, self.AppStateManager, 6)
        self.animation = Animation(self.screen, self.AppStateManager)

        # self.states = {'wb_cartogram': self.wb_cartogram}
        # self.states = {'color_cartogram': self.color_cartogram}
        # self.states = {'case_1': self.case_1}
        self.states = {'animation' : self.animation}

        # self.states = {'start': self.start,
        #                'wb_cartogram': self.wb_cartogram,
        #                'color_cartogram': self.color_cartogram,
        #                'case_1': self.case_1,
        #                'case_2': self.case_2,
        #                'case_3': self.case_3,
        #                'case_4': self.case_4,
        #                'case_5': self.case_5,
        #                'case_6': self.case_6,
        #                'animation': self.animation}

    def run(self):
        print("App running")
        os.makedirs("pics", exist_ok=True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        # pygame.image.save(self.screen, "pics/WB_cartogramm.jpeg")
                        # pygame.image.save(self.screen, "pics/Color_cartogramm.jpeg")
                        pygame.image.save(self.screen, "pics/Case.jpeg")
                        pygame.quit()
                        sys.exit()

            self.states[self.AppStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(30)

# class Start:
#     def __init__(self, display, AppStateManager):
#         self.display = display
#         self.AppStateManager = AppStateManager
#
#     def run(self):
#         self.display.fill(WHITE)
#         self.display.blit(menu(), (W / 2, H / 2))
#
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_1]:
#             self.AppStateManager.set_state('case_1')
#         if keys[pygame.K_2]:
#             self.AppStateManager.set_state('case_2')
#         if keys[pygame.K_3]:
#             self.AppStateManager.set_state('case_3')
#         if keys[pygame.K_4]:
#             self.AppStateManager.set_state('case_4')
#         if keys[pygame.K_5]:
#             self.AppStateManager.set_state('case_5')
#         if keys[pygame.K_6]:
#             self.AppStateManager.set_state('case_6')
#
#         if keys[pygame.K_8]:
#             self.AppStateManager.set_state('wb_cartogram')
#         if keys[pygame.K_9]:
#             self.AppStateManager.set_state('color_cartogram')
#         if keys[pygame.K_0]:
#             self.display.fill(WHITE)
#             self.AppStateManager.set_state('animation')

class WB_cartogram:
    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager

        # self.tmp_surf = pygame.Surface((W, H))

    def run(self):
        self.display.fill(WHITE)
        az_cells = make_cartogram('wb')
        for cell in az_cells:
            cell.draw_hex_area(self.display)
        # self.display.blit(axes, (0.75 * W, 0.70 * H))

class Color_cartogram:
    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager

    def run(self):
        self.display.fill(WHITE)
        az_cells = make_cartogram('color')
        for cell in az_cells:
            cell.draw_hex_area(self.display)

class Case:
    def __init__(self, display, AppStateManager, case_number):
        self.display = display
        self.AppStateManager = AppStateManager
        self.case_number = case_number

    def run(self):
        self.display.fill(WHITE)
        case_cells = make_case(1)
        pygame.draw.aalines(self.display, BLACK, True, make_case_outline())
        for cell in case_cells:
            cell.draw_hex_area_invert(self.display)

class Animation():

    def __init__(self, display, AppStateManager):
        self.display = display
        self.AppStateManager = AppStateManager
        self.m = 0

    def run(self):
        self.display.fill(WHITE)
        isRunning = 1
        while isRunning:
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()
                    # if(event.key == pygame.K_ESCAPE):
                    #     self.AppStateManager.set_state('start')
                    #     self.m = 0
                    #     isRunning = False
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




