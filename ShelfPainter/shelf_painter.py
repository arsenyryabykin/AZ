import sys
import pygame
from config import W, H
from shelf import make_shelf

class App:
    def __init__(self):
        pygame.init()
        #self.screen = pygame.display.set_mode((W, H), pygame.SCALED)
        self.surf = pygame.Surface((W, H))
        # self.clock = pygame.time.Clock()

    def run(self):

        print("App running")
        shelf_1 = make_shelf(self.surf, 1)      # Создание объекта стеллажа
        shelf_2 = make_shelf(self.surf, 2)      # Создание объекта стеллажа
        shelf_3 = make_shelf(self.surf, 3)      # Создание объекта стеллажа

        # Цикл приложения
        # while True:
            # for event in pygame.event.get():
            #     #pos = pygame.mouse.get_pos()
            #
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #
            #     if(event.type == pygame.KEYDOWN):
            #         if(event.key == pygame.K_q):
            #             pygame.quit()
            #             sys.exit()

                    # elif(event.key == pygame.K_s):
                    #     pygame.image.save(self.screen, "screenshot.png")

            # Отрисовка стеллажей ##############################################

        self.surf.fill((255,255,255))
        for cell in shelf_1:
            cell.draw_hex_area(self.surf)
        pygame.image.save(self.surf, "shelf_1.png")


        self.surf.fill((255, 255, 255))
        for cell in shelf_2:
            cell.draw_hex_area(self.surf)
        pygame.image.save(self.surf, "shelf_2.png")

        self.surf.fill((255, 255, 255))
        for cell in shelf_3:
            cell.draw_hex_area(self.surf)
        pygame.image.save(self.surf, "shelf_3.png")

        print("App finished")
        pygame.quit()
        sys.exit()

            #######################################################################

            # pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.run()




