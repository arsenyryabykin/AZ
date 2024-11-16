import sys
import pygame
from Cell import Cell
from random import randint
import itertools

W = 1280
H = 1024

class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED)

        self.clock = pygame.time.Clock()

        self.colors = [(255, 255, 255), (255, 17, 0)]

    def run(self):
        print("App running")
       # self.cells = [Cell(self.screen, 1, 60, (W / 2, H / 2)), Cell(self.screen, 2, 60, (W / 2 - 200, H / 2))]
        self.cell = Cell(self.screen, 1, 30, (W / 2, H / 2))
        counter = 0
        while True:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()

                # elif(event.type == pygame.MOUSEMOTION):
                #     if(self.cell.clicked_zone.collidepoint(pos)):
                #         self.cell.is_hovered = True
                #     else:
                #         self.cell.is_hovered = False

                elif(event.type == pygame.MOUSEBUTTONUP):
                    if(self.cell.clicked_zone.collidepoint(pos)):
                        self.cell.is_activated = True if (not self.cell.is_activated) else False

                    # for element in self.cells:
                    #     if(element.clicked_zone.collidepoint(pos)):# self.cell.clicked_zone.collidepoint(pos)):
                    #         element.is_activated = True if (not element.is_activated) else False
                    #        # self.cell.is_activated = True if (not self.cell.is_activated) else False

                #elif(event.type == pygame.MOUSEBUTTONUP):
                    #self.cell.is_activated = True if (not self.cell.is_activated) else False

            self.screen.fill((255, 255, 255))
            self.cell.draw_hex_area(self.screen)
            # for element in self.cells:
            #     element.draw_hex_area(self.screen)# self.cell.draw_hex_area(self.screen)

            counter += 1
            print(counter, self.cell.color)
            if(counter > 15 and self.cell.is_activated):
                #self.cell.color = itertools.cycle(self.colors)
                self.cell.color = self.colors[0] if (self.cell.color != self.colors[0]) else self.colors[1]
                counter = 0
            pygame.display.update()
            self.clock.tick(30)


if __name__ == '__main__':
    app = App()
    app.run()




