import pygame
from math import sqrt, ceil
import sqlite3
from enum import Enum
from case_lattice import dx, dy, radius, x0, y0
from config import BLACK, WHITE

shelf_1 = []; shelf_2 = []; shelf_3 = []
case_1 = []; case_2 = []; case_3 = []; case_4 = []; case_5 = []; case_6 = []; case_7 = []
az = []

shelf_coords = ['А1','А2','А3','А4','А5','А6','А7','А8','А9','А10',
          'Б1','Б2','Б3','Б4','Б5','Б6','Б7','Б8','Б9',
          'В1','В2','В3','В4','В5','В6','В7','В8','В9','В10',
          'Г1','Г2','Г3','Г4','Г5','Г6','Г7','Г8','Г9',
          'Д1','Д2','Д3','Д4','Д5','Д6','Д7','Д8','Д9','Д10',
          'Е1','Е2','Е3','Е4','Е5','Е6','Е7','Е8','Е9',
          'Ж1','Ж2','Ж3','Ж4','Ж5','Ж6','Ж7','Ж8','Ж9','Ж10']

load_schedule = []
with open('load_schedule.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        result = line.split()

        load_schedule.append(result)

case_content = [load_schedule[0:27],
                load_schedule[27:54],
                load_schedule[54:81],
                load_schedule[81:108],
                load_schedule[108:135],
                load_schedule[135:162],
                load_schedule[162:]]


def draw_hex_area(Surface, color, border_color, radius, position, width = 1):
    line_coords = []
    line_coords.append((position[0], position[1] + 2 * radius/ sqrt(3)))
    line_coords.append((position[0] + radius, position[1] + radius /sqrt(3)))
    line_coords.append((position[0] + radius, position[1] - radius /sqrt(3)))
    line_coords.append((position[0], position[1] - 2 * radius/ sqrt(3)))
    line_coords.append((position[0] - radius, position[1] - radius/sqrt(3)))
    line_coords.append((position[0] - radius, position[1] + radius/sqrt(3)))

    coords = []
    coords.append((position[0], position[1] + 2 * radius/ sqrt(3)))
    coords.append((position[0] + radius, position[1] + radius /sqrt(3)))
    coords.append((position[0] + radius, position[1] - radius /sqrt(3)))
    coords.append((position[0], position[1] - 2 * radius/ sqrt(3)))
    coords.append((position[0] - radius, position[1] - radius/sqrt(3)))
    coords.append((position[0] - radius, position[1] + radius/sqrt(3)))

    pygame.draw.polygon(Surface, color, coords)
    pygame.draw.aalines(Surface, border_color, True, line_coords)

def draw_case(Surface, color, border_color, radius, position):
    wall_coords = []
    wall_coords.append((x0 + 3.1*dx, y0 - (dy + radius)))
    wall_coords.append((x0 + 2.5*dx, y0 - 2.65*dy))
    wall_coords.append((x0 - 2.5*dx, y0 - 2.65*dy))
    wall_coords.append((x0 - 3.1*dx, y0 - (dy + radius)))
    wall_coords.append((x0 - 3.1*dx, y0 + (dy + radius)))
    wall_coords.append((x0 - 2.5*dx, y0 + 2.65*dy))
    wall_coords.append((x0 + 2.5*dx, y0 + 2.65*dy))
    wall_coords.append((x0 + 3.1*dx, y0 + (dy + radius)))

    # pygame.draw.polygon(Surface, color, wall_coords)
    pygame.draw.aalines(Surface, border_color, True, wall_coords)




def draw_hex_area_invert(Surface, color, border_color, radius, position):

    line_coords = []
    line_coords.append((position[0] + 2*radius/sqrt(3), position[1]))
    line_coords.append((position[0] + radius/sqrt(3), position[1] - radius))
    line_coords.append((position[0] - radius/sqrt(3), position[1] - radius))
    line_coords.append((position[0] - 2*radius/sqrt(3), position[1]))
    line_coords.append((position[0] - radius/sqrt(3), position[1] + radius))
    line_coords.append((position[0] + radius/sqrt(3), position[1] + radius))

    # coords = []
    # coords.append((position[0], position[1] + 2 * radius/ sqrt(3)))
    # coords.append((position[0] + radius, position[1] + radius /sqrt(3)))
    # coords.append((position[0] + radius, position[1] - radius /sqrt(3)))
    # coords.append((position[0], position[1] - 2 * radius/ sqrt(3)))
    # coords.append((position[0] - radius, position[1] - radius/sqrt(3)))
    # coords.append((position[0] - radius, position[1] + radius/sqrt(3)))

    pygame.draw.polygon(Surface, color, line_coords)
    pygame.draw.aalines(Surface, border_color, True, line_coords)


# Запрос данных из БД по загрузке АЗ
def get_az_data() -> dict:
    conn = sqlite3.connect('imitators.db')
    cur = conn.cursor()

    cur.execute('''SELECT az_coordinate_to, tvs_number, suz_number, case_number_from
                FROM az_operations''')
    data = cur.fetchall()

    text_az_data = {}
    for coord, tvs, suz, case in data:
        text_az_data[coord] = (tvs, suz, case) # Получение данных из БД в формате {id :(ТВС, СУЗ, номер чехла)

    return text_az_data


# Запрос данных из БД по загрузке чехла i
def get_case_data(case_number):
    conn = sqlite3.connect('imitators.db')
    cur = conn.cursor()

    cur.execute('''SELECT case_coordinate, tvs_number, suz_number
                   FROM cases
                   WHERE case_number = ?''', (str(case_number)))
    data = cur.fetchall()

    text_case_data = {}
    for coord, tvs, suz in data:
        text_case_data[coord] = (tvs, suz)  # Получение данных из БД в формате {id :(ТВС, СУЗ)

    return text_case_data


# Заполнение ячеек текстом из БД
def text_box(tvs_text, suz_text, color, color_bg, font_size):

    if(suz_text == None):
        suz_text = "        "
    f_sys = pygame.font.SysFont('tflextypea', font_size)
    text_1 = f_sys.render(tvs_text, 1, color, color_bg)
    text_2 = f_sys.render(suz_text, 1, color, color_bg)
    res_text = pygame.Surface((text_1.get_width(), 2 * text_1.get_height()))
    res_text.fill(color_bg)
    res_text.blit(text_1, (0,0))
    res_text.blit(text_2, (0, text_1.get_height()))
    return res_text

def text(text, color, color_bg, font_size, bold = False):

    if bold:
        f_sys = pygame.font.SysFont('tflextypea', font_size, True)
    else:
        f_sys = pygame.font.SysFont('tflextypea', font_size)
    text = f_sys.render(text, 1, color, color_bg)

    return text

def make_case_labels():
    f_sys = pygame.font.SysFont('tflextypea', 30)

    label_1 = f_sys.render('Чехол 1', 1, (0,0,0), colors[1])
    label_2 = f_sys.render('Чехол 2', 1, (0,0,0), colors[2])
    label_3 = f_sys.render('Чехол 3', 1, (0,0,0), colors[3])
    label_4 = f_sys.render('Чехол 4', 1, (0,0,0), colors[4])
    label_5 = f_sys.render('Чехол 5', 1, (0,0,0), colors[5])
    label_6 = f_sys.render('Чехол 6', 1, (0,0,0), colors[6])
    label_7 = f_sys.render('Чехол 7', 1, (0,0,0), colors[7])

    res_text = pygame.Surface((label_7.get_width(), 7 * label_7.get_height()))
    res_text.fill(WHITE)
    res_text.blit(label_1, (0,0))
    res_text.blit(label_2, (0, 1*label_1.get_height()))
    res_text.blit(label_3, (0, 2*label_1.get_height()))
    res_text.blit(label_4, (0, 3*label_1.get_height()))
    res_text.blit(label_5, (0, 4*label_1.get_height()))
    res_text.blit(label_6, (0, 5*label_1.get_height()))
    res_text.blit(label_7, (0, 6*label_1.get_height()))

    return res_text

def menu():
    f_sys = pygame.font.SysFont('tflextypea', 30)

    label_1 = f_sys.render('1 - Чехол 1', 1, BLACK, WHITE)
    label_2 = f_sys.render('2 - Чехол 2', 1, BLACK, WHITE)
    label_3 = f_sys.render('3 - Чехол 3', 1, BLACK, WHITE)
    label_4 = f_sys.render('4 - Чехол 4', 1, BLACK, WHITE)
    label_5 = f_sys.render('5 - Чехол 5', 1, BLACK, WHITE)
    label_6 = f_sys.render('6 - Чехол 6', 1, BLACK, WHITE)
    label_7 = f_sys.render('7 - Чехол 7', 1, BLACK, WHITE)
    label_8 = f_sys.render('8 - Картограмма ч/б', 1, BLACK, WHITE)
    label_9 = f_sys.render('9 - Картограмма цвет', 1, BLACK, WHITE)
    label_10 = f_sys.render('0 - Анимация', 1, BLACK, WHITE)


    res_text = pygame.Surface((label_9.get_width(), 10 * label_9.get_height()))
    res_text.fill(WHITE)
    res_text.blit(label_1, (0,0))
    res_text.blit(label_2, (0, 1*label_1.get_height()))
    res_text.blit(label_3, (0, 2*label_1.get_height()))
    res_text.blit(label_4, (0, 3*label_1.get_height()))
    res_text.blit(label_5, (0, 4*label_1.get_height()))
    res_text.blit(label_6, (0, 5*label_1.get_height()))
    res_text.blit(label_7, (0, 6*label_1.get_height()))
    res_text.blit(label_8, (0, 7 * label_1.get_height()))
    res_text.blit(label_9, (0, 8 * label_1.get_height()))
    res_text.blit(label_10, (0, 9 * label_1.get_height()))


    return res_text


def save(display, file_name):
    pygame.image.save(display, file_name)

colors = {1 : (255, 255, 0),
2 : (219, 112, 147),
3 : (0, 191, 255),
4 : (192, 192, 192),
5 : (220, 20, 60),
6 : (152, 251, 152),
7 : (255, 165, 0)}


print(get_case_data(7))
