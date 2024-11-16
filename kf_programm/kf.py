import sys
import pygame
from az import make_az
from Cell import Cell
from random import randint

from config import W, H, radius

class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

        self.colors = [(255, 255, 255), (255, 17, 0)]

    def run(self):
        print("App running")


        self.cell = Cell(self.screen, 1, radius, (W / 2, H / 2), ("N00111И1", "N0111И1"))
        self.cell.is_installed = True
        # self.cells = make_az(self.screen)
        # self.cells[0].is_installed = True
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

                # Использовать мигание для чехла, не для зоны
                elif(event.type == pygame.MOUSEBUTTONUP):
                    # if(self.cell.clicked_zone.collidepoint(pos)):
                    #     self.cell.is_activated = True if (not self.cell.is_activated) else False

                    for cell in self.cells:
                        if(cell.clicked_zone.collidepoint(pos)):
                            cell.is_activated = True if (not cell.is_activated) else False



            self.screen.fill((255, 255, 255))
            self.cell.draw_hex_area(self.screen)
            # self.cell1.draw_hex_area(self.screen)

            # for cell in self.cells:
            #     cell.draw_hex_area(self.screen)


            # counter += 1
            # if(counter > 15 and self.cell.is_activated):
            #     #self.cell.color = itertools.cycle(self.colors)
            #     self.cell.color = self.colors[0] if (self.cell.color != self.colors[0]) else self.colors[1]
            #     counter = 0

            pygame.display.update()
            self.clock.tick(30)


if __name__ == '__main__':
    app = App()
    app.run()




