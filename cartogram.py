import sys
import pygame
from common import draw_hex_area, draw_hex_area_invert, draw_case, text_box, get_az_data, colors, get_case_data
from az_lattice import az_coords
from case_lattice import case_coords, case_cells_coords
from resources import W, H, radius
from resources import BLACK, WHITE, axes
from common import load_schedule
from common import make_case_labels
import buttons


FPS = 30

pygame.init()

sc = pygame.display.set_mode((W, H), pygame.SCALED | pygame.RESIZABLE)
sc.fill(WHITE)

pygame.display.set_caption("Картограмма")

clock = pygame.time.Clock()

def make_cartogram(type = 'wb'):
    print("Отрисовка картограммы")
    # Получить данные по координатам и ТВС из БД
    text_az_data = get_az_data()

    sc.blit(axes, (0.75 * W, 0.70 * H))

    # Отрисовка картограммы и текста
    for key, value in az_coords.items():
        tmp_text = text_az_data[key]
        if(type == 'wb'):
            color_bg = WHITE
        elif(type == 'colored'):
            color_bg = colors[tmp_text[2]]
            sc.blit(make_case_labels(), (W/2 + 16*radius, H/2))

        res = text_box(tmp_text[0], tmp_text[1], BLACK, color_bg, 22)
        draw_hex_area(sc, color_bg, BLACK, radius, value, 1)
        sc.blit(res, (value[0] - res.get_width() / 2, value[1] - res.get_height() / 2))


b = buttons.Button(W/2, H/2, 400, 100, 'Картограмма Ч/Б', make_cartogram('wb'))

az_data = get_az_data()
def animation(i):
    position = load_schedule[i][0]
    print(position)
    coord = az_coords[position]
    tmp_text = az_data[position]
    color_bg = colors[tmp_text[2]]
    print(color_bg)
    print()
    # res = text_box(tmp_text[0], tmp_text[1], BLACK, color_bg, 22)
    draw_hex_area(sc, color_bg, BLACK, radius, coord)
    # sc.blit(res, (value[0] - res.get_width() / 2, value[1] - res.get_height() / 2))


def make_case(case_number):
    f_sys = pygame.font.SysFont('tflextypea', 20)

    case_data = get_case_data(case_number)
    draw_case(sc, WHITE, BLACK, 60, (W/2, H/2))
    for key, value in case_cells_coords.items():
        case_cell_text = f_sys.render(key, 1, BLACK, WHITE)    # Текст с номером ячейки чехла
        sc.blit(case_cell_text, (value[0] - case_cell_text.get_width() / 2, value[1] - case_cell_text.get_height() / 2))

    sc.blit(axes, (0.75*W, 0.70*H))

    for key, value in case_coords.items():
        tmp_text = case_data[key]
        res = text_box(tmp_text[0], tmp_text[1], BLACK, WHITE, 24)
        draw_hex_area_invert(sc, WHITE, BLACK, 60, value)
        sc.blit(res, (value[0] - res.get_width() / 2, value[1] - res.get_height() / 2))

i = 0
def save(file_name):
    pygame.image.save(sc, file_name)


sc.fill(WHITE)


flRunning = True
while flRunning:
    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            flRunning = False
            sys.exit()

    b.process(sc)

    save('1.png')


        # elif(event.type == pygame.KEYDOWN):
        #     if(event.key == pygame.K_0):
        #         sc.fill(WHITE)
        #         make_cartogram('wb')
        #         save('wb_cartogram.png')
        #     if(event.key == pygame.K_9):
        #         sc.fill(WHITE)
        #         make_cartogram('colored')
        #         save('colored_cartogram.png')
        #     if (event.key == pygame.K_1):
        #         sc.fill(WHITE)
        #         make_case(6)
        #         save('case.png')
        #     if(event.key == pygame.K_8):
        #         sc.fill(WHITE)
        #         while 1:
        #             for event in pygame.event.get():
        #                 if(event.type == pygame.KEYDOWN):
        #                     if (event.key == pygame.K_PLUS):
        #                         animation(i)
        #                         i = i + 1



    pygame.display.update()  # Буферизация вывода графической информации
    clock.tick(FPS)