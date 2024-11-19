import sys
import pygame
from config import W, H

from shelf import make_shelf

class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()


    def run(self):
        print("App running")


        shelf = make_shelf(self.screen)
        print(shelf)


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
                    elif(event.key == pygame.K_s):
                        pygame.image.save(self.screen, "screenshot.png")

            ##### Отрисовка ########################################################
            self.screen.fill((255,255,255))
            for cell in shelf:
                cell.draw_hex_area(self.screen)
            #######################################################################

            pygame.display.update()
            self.clock.tick(30)


if __name__ == '__main__':
    app = App()
    app.run()




