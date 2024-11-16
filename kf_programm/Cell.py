import pygame
from math import sqrt


class Cell:

    def __init__(self, Surface, id, radius, position):
        self.id = id
        self.radius = radius
        self.position = position
        self.color = (255, 255, 255)
        self.border_color = (0,0,0)
        #self.rect = pygame.Rect((position[0] - radius, position[1] - radius / sqrt(3)), (2 * radius, 2 * radius / sqrt(3)))
        self.text_surface = pygame.Surface((2 * radius, 2 * radius / sqrt(3)))
        self.clicked_zone = pygame.Rect((self.position[0] - self.radius, self.position[1] - self.radius / sqrt(3)), (2 * self.radius, 2 * self.radius / sqrt(3)))


        self.is_activated = False
        self.is_hovered = False


    # def check_color(self):
    #     if(self.is_hovered):
    #         self.color = (255, 255, 50)
    #     else:
    #         self.color = (255, 255, 255)

    def draw_hex_area(self, Surface):
        line_coords = []
        line_coords.append((self.position[0], self.position[1] + 2 * self.radius/ sqrt(3)))
        line_coords.append((self.position[0] + self.radius, self.position[1] + self.radius /sqrt(3)))
        line_coords.append((self.position[0] + self.radius, self.position[1] - self.radius /sqrt(3)))
        line_coords.append((self.position[0], self.position[1] - 2 * self.radius/ sqrt(3)))
        line_coords.append((self.position[0] - self.radius, self.position[1] - self.radius/sqrt(3)))
        line_coords.append((self.position[0] - self.radius, self.position[1] + self.radius/sqrt(3)))

        coords = []
        coords.append((self.position[0], self.position[1] + 2 * self.radius/ sqrt(3)))
        coords.append((self.position[0] + self.radius, self.position[1] + self.radius /sqrt(3)))
        coords.append((self.position[0] + self.radius, self.position[1] - self.radius /sqrt(3)))
        coords.append((self.position[0], self.position[1] - 2 * self.radius/ sqrt(3)))
        coords.append((self.position[0] - self.radius, self.position[1] - self.radius/sqrt(3)))
        coords.append((self.position[0] - self.radius, self.position[1] + self.radius/sqrt(3)))

        # self.check_color()

        pygame.draw.polygon(Surface, self.color, coords)
        pygame.draw.aalines(Surface, self.border_color, True, line_coords)


        # res = text_box("N00654I1", None, (0,0,0), (255,255,255), 12)

        f_sys = pygame.font.SysFont('tflextypea', 16)
        text_1 = f_sys.render("N00111И1", 1, (0, 0, 0))
        text_2 = f_sys.render("N0111И1", 1, (0, 0, 0))

        midtop = self.clicked_zone.midtop
        midbottom = self.clicked_zone.midbottom
        place1 = text_1.get_rect(midbottom=self.position)
        place2 = text_2.get_rect(midtop=self.position)


        Surface.blit(text_1, place1)
        Surface.blit(text_2, place2)








# Заполнение ячеек текстом из БД
def text_box(tvs_text, suz_text, color, color_bg, font_size):
    if (suz_text == None):
        suz_text = "        "
    f_sys = pygame.font.SysFont('tflextypea', font_size)
    text_1 = f_sys.render(tvs_text, 1, color, color_bg)
    text_2 = f_sys.render(suz_text, 1, color, color_bg)
    res_text = pygame.Surface((text_1.get_width(), 2 * text_1.get_height()))
    res_text.fill(color_bg)
    res_text.blit(text_1, (0, 0))
    res_text.blit(text_2, (0, text_1.get_height()))
    return res_text