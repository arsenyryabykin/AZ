import pygame
from math import sqrt


class Cell:

    def __init__(self, Surface, id, radius, position, text=(None, None)):
        self.id = id
        self.radius = radius
        self.position = position
        self.tvs_text = text[0]
        self.suz_text = text[1] if text[1] is not None else " "
        self.color = (255, 255, 255)
        self.border_color = (0,0,0)
        self.clicked_zone = pygame.Rect((self.position[0] - self.radius, self.position[1] - self.radius / sqrt(3)), (2 * self.radius, 2 * self.radius / sqrt(3)))

        self.is_activated = False
        self.is_hovered = False
        self.is_installed = False


    # def check_color(self):
    #     if(self.is_hovered):
    #         self.color = (255, 255, 50)
    #     else:
    #         self.color = (255, 255, 255)

    def draw_hex_area(self, Surface):
        line_coords = []
        # line_coords.append((self.position[0], self.position[1] + 2 * self.radius/ sqrt(3)))
        # line_coords.append((self.position[0] + self.radius, self.position[1] + self.radius /sqrt(3)))
        # line_coords.append((self.position[0] + self.radius, self.position[1] - self.radius /sqrt(3)))
        # line_coords.append((self.position[0], self.position[1] - 2 * self.radius/ sqrt(3)))
        # line_coords.append((self.position[0] - self.radius, self.position[1] - self.radius/sqrt(3)))
        # line_coords.append((self.position[0] - self.radius, self.position[1] + self.radius/sqrt(3)))

        line_coords.append((self.position[0] + self.radius, self.position[1]))
        line_coords.append((self.position[0] + 2*self.radius, self.position[1] + self.radius/sqrt(3)))
        line_coords.append((self.position[0] + 2*self.radius, self.position[1] + 3*self.radius/sqrt(3)))
        line_coords.append((self.position[0] + self.radius, self.position[1] + 4 * self.radius/ sqrt(3)))
        line_coords.append((self.position[0], self.position[1] + 3*self.radius/sqrt(3)))
        line_coords.append((self.position[0], self.position[1] + self.radius/sqrt(3)))


        coords = []
        # coords.append((self.position[0], self.position[1] + 2 * self.radius/ sqrt(3)))
        # coords.append((self.position[0] + self.radius, self.position[1] + self.radius /sqrt(3)))
        # coords.append((self.position[0] + self.radius, self.position[1] - self.radius /sqrt(3)))
        # coords.append((self.position[0], self.position[1] - 2 * self.radius/ sqrt(3)))
        # coords.append((self.position[0] - self.radius, self.position[1] - self.radius/sqrt(3)))
        # coords.append((self.position[0] - self.radius, self.position[1] + self.radius/sqrt(3)))

        coords.append((self.position[0] + self.radius, self.position[1]))
        coords.append((self.position[0] + 2*self.radius, self.position[1] + self.radius/sqrt(3)))
        coords.append((self.position[0] + 2*self.radius, self.position[1] + 3*self.radius/sqrt(3)))
        coords.append((self.position[0] + self.radius, self.position[1] + 4 * self.radius/ sqrt(3)))
        coords.append((self.position[0], self.position[1] + 3*self.radius/sqrt(3)))
        coords.append((self.position[0], self.position[1] + self.radius/sqrt(3)))



        # self.check_color()

        if(not self.is_activated):
            self.color = (255,255,255)

        pygame.draw.polygon(Surface, self.color, coords)
        pygame.draw.aalines(Surface, self.border_color, True, line_coords)


        #if(self.tvs_text is not None):
        if(self.is_installed):
            f_sys = pygame.font.SysFont('tflextypea', 20)
            text_1 = f_sys.render(self.tvs_text, 1, (0, 0, 0))
            text_2 = f_sys.render(self.suz_text, 1, (0, 0, 0))

            place1 = text_1.get_rect(midbottom=self.position)
            place2 = text_2.get_rect(midtop=self.position)

            Surface.blit(text_1, place1)
            Surface.blit(text_2, place2)
