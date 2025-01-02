import sys
import os
import pygame
from config import W, H
from shelf import make_shelf
from shelf_content import check_unique

class App:
    def __init__(self):
        pygame.init()
        self.surf = pygame.Surface((W, H))

    def run(self):

        shelves = [make_shelf(self.surf, i) for i in range(1,4)]  # Создание стеллажей
        check_unique(shelves)   # Поиск повторов в стеллажах
        os.makedirs("pics", exist_ok=True)

        for i, shelf in enumerate(shelves, 1):
            self.surf.fill((255,255,255))
            for cell in shelf:
                cell.draw_hex_area(self.surf)
            pygame.image.save(self.surf, "pics/Стеллаж_70" + str(i) + ".png")

        pygame.quit()
        sys.exit()


app = App()
app.run()




