import pygame
from math import sqrt
from config import font_size, index_font_size
from os import path
from config import WHITE


class Cell:
    """
        Класс, описывающий элементарную ячейку для любого объекта ТТО - активной зоны, чехла, стеллажа.
        ...
        Атрибуты
        --------
        id : str
            строковая координата в собственной системе координат объекта (14-25; 1,2,3...; А6, Ж8...)
        radius : int
            радиус вписанной окружности шестигранника
        position : tuple(x, y)
            координата ячейки в системе координат поверхности pygame
        tvs_text : str
            идентификационный номер ИТВС / ТВС
        suz_text : str
            идентификационный номер ИПС СУЗ / ПС СУЗ
        color : tuple(r,g,b)
            цвет ячейки
        border_color : tuple(r,g,b)
            цвет границ ячейки
        Методы
        ------
        """
    def __init__(self, id, radius, position, text=(None, None), color = WHITE):
        """
         Устанавливает все необходимые атрибуты для объекта Cell.
         Параметры
         ---------
         name : id
                 строковая координата в собственной системе координат объекта (14-25; 1,2,3...; А6, Ж8...)
        radius : int
            радиус вписанной окружности шестигранника
        position : tuple(x, y)
            координата ячейки в системе координат поверхности pygame
        text : tuple(str, str)
            идентификационные номера содержимого ячейки - ТВС/ИТВС, ПС СУЗ/ИПС СУЗ
        color : tuple(r,g,b)
            цвет ячейки
         """
        self.id = id
        self.radius = radius
        self.position = position
        self.tvs_text = text[0]
        self.suz_text = text[1] if text[1] is not None else " "
        self.color = color
        self.border_color = (0,0,0)
        self.is_installed = True

    def draw_hex_area(self, surface):
        """
           Отрисовка шестигранника в y-ориентации
                   Параметры:
                           surface (pygame.surface): поверхность для отрисовки
        """
        line_coords = []
        line_coords.append((self.position[0], self.position[1] + 2 * self.radius/ sqrt(3)))
        line_coords.append((self.position[0] + self.radius, self.position[1] + self.radius /sqrt(3)))
        line_coords.append((self.position[0] + self.radius, self.position[1] - self.radius /sqrt(3)))
        line_coords.append((self.position[0], self.position[1] - 2 * self.radius/ sqrt(3)))
        line_coords.append((self.position[0] - self.radius, self.position[1] - self.radius/sqrt(3)))
        line_coords.append((self.position[0] - self.radius, self.position[1] + self.radius/sqrt(3)))

        # polygon_coords = line_coords   удалить после теста

        # line_coords.append((self.position[0] + self.radius, self.position[1]))
        # line_coords.append((self.position[0] + 2*self.radius, self.position[1] + self.radius/sqrt(3)))
        # line_coords.append((self.position[0] + 2*self.radius, self.position[1] + 3*self.radius/sqrt(3)))
        # line_coords.append((self.position[0] + self.radius, self.position[1] + 4 * self.radius/ sqrt(3)))
        # line_coords.append((self.position[0], self.position[1] + 3*self.radius/sqrt(3)))
        # line_coords.append((self.position[0], self.position[1] + self.radius/sqrt(3)))
        # polygon_coords = line_coords

        # Отрисовка по заданным координатам полигона и обводки
        # pygame.draw.polygon(Surface, self.color, polygon_coords) удалить после теста
        pygame.draw.polygon(surface, self.color, line_coords)
        pygame.draw.aalines(surface, self.border_color, True, line_coords)

        # Работа с текстом
        f_sys_index = pygame.font.Font('font.ttf', index_font_size) if path.exists('font.ttf') else pygame.font.SysFont('timesnewroman', index_font_size)
        text_index = f_sys_index.render(self.id, 1, (0,0,0))
        index_place = text_index.get_rect(midbottom=(self.position[0], self.position[1] + 2 * self.radius/ sqrt(3) - 10))
        surface.blit(text_index, index_place)


        if(self.is_installed):
            f_sys = pygame.font.Font('font.ttf', font_size) if path.exists('font.ttf') else pygame.font.SysFont('timesnewroman', font_size)
            text_1 = f_sys.render(self.tvs_text, 1, (0, 0, 0))
            text_2 = f_sys.render(self.suz_text, 1, (0, 0, 0))

            place1 = text_1.get_rect(midbottom=self.position)
            place2 = text_2.get_rect(midtop=self.position)

            surface.blit(text_1, place1)
            surface.blit(text_2, place2)


    def draw_hex_area_invert(self, surface):
        """
           Отрисовка шестигранника в x-ориентации
                   Параметры:
                           Surface (pygame.surface): поверхность для отрисовки
        """
        line_coords = []
        line_coords.append((self.position[0] + 2*self.radius/sqrt(3), self.position[1]))
        line_coords.append((self.position[0] + self.radius/sqrt(3), self.position[1] - self.radius))
        line_coords.append((self.position[0] - self.radius/sqrt(3), self.position[1] - self.radius))
        line_coords.append((self.position[0] - 2*self.radius/sqrt(3), self.position[1]))
        line_coords.append((self.position[0] - self.radius/sqrt(3), self.position[1] + self.radius))
        line_coords.append((self.position[0] + self.radius/sqrt(3), self.position[1] + self.radius))

        # coords = []
        # coords.append((position[0], position[1] + 2 * radius/ sqrt(3)))
        # coords.append((position[0] + radius, position[1] + radius /sqrt(3)))
        # coords.append((position[0] + radius, position[1] - radius /sqrt(3)))
        # coords.append((position[0], position[1] - 2 * radius/ sqrt(3)))
        # coords.append((position[0] - radius, position[1] - radius/sqrt(3)))
        # coords.append((position[0] - radius, position[1] + radius/sqrt(3)))

        # Отрисовка по заданным координатам полигона и обводки
        pygame.draw.polygon(surface, self.color, line_coords)
        pygame.draw.aalines(surface, self.border_color, True, line_coords)

        # Работа с текстом
        f_sys_index = pygame.font.Font('font.ttf', index_font_size) if path.exists('font.ttf') else pygame.font.SysFont('timesnewroman', index_font_size)
        text_index = f_sys_index.render(self.id, 1, (0,0,0))
        index_place = text_index.get_rect(midbottom=(self.position[0], self.position[1] + 2 * self.radius/ sqrt(3) - 10))
        surface.blit(text_index, index_place)


        if(self.is_installed):
            f_sys = pygame.font.Font('font.ttf', font_size) if path.exists('font.ttf') else pygame.font.SysFont('timesnewroman', font_size)
            text_1 = f_sys.render(self.tvs_text, 1, (0, 0, 0))
            text_2 = f_sys.render(self.suz_text, 1, (0, 0, 0))

            place1 = text_1.get_rect(midbottom=self.position)
            place2 = text_2.get_rect(midtop=self.position)

            surface.blit(text_1, place1)
            surface.blit(text_2, place2)
