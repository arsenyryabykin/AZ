from resources import BLACK, WHITE, axes, W, H, radius
from common import draw_hex_area, draw_hex_area_invert, draw_case, text_box, get_az_data, colors, get_case_data
from az_lattice import az_coords
from common import make_case_labels, text, load_schedule, get_az_data
from case_lattice import case_coords, case_cells_coords



az_data = get_az_data()


#########################################################
def make_cartogram(display, type = 'wb'):
    # Получить данные по координатам и ТВС из БД
    text_az_data = get_az_data()

    display.blit(axes, (0.75 * W, 0.70 * H))

    # Отрисовка картограммы и текста
    for key, value in az_coords.items():
        tmp_text = text_az_data[key]
        if(type == 'wb'):
            color_bg = WHITE
        elif(type == 'colored'):
            color_bg = colors[tmp_text[2]]
            display.blit(make_case_labels(), (W/2 + 16*radius, H/2))

        res = text_box(tmp_text[0], tmp_text[1], BLACK, color_bg, 22)
        draw_hex_area(display, color_bg, BLACK, radius, value, 1)
        display.blit(res, (value[0] - res.get_width() / 2, value[1] - res.get_height() / 2))

######################################################3
def make_case(display, case_number):

    case_data = get_case_data(case_number)  # Получить данные по чехлам из БД для отрисовки
    draw_case(display, WHITE, BLACK, 60, (W / 2, H / 2))    # Отрисовка корпуса чехла

    for key, value in case_coords.items():
        tmp_text = case_data[key]
        res = text_box(tmp_text[0], tmp_text[1], BLACK, WHITE, 24)
        draw_hex_area_invert(display, WHITE, BLACK, 60, value)
        display.blit(res, (value[0] - res.get_width() / 2, value[1] - res.get_height() / 2))

    for key, value in case_cells_coords.items():
        # case_cell_text = f_sys.render(key, 1, BLACK, WHITE)  # Текст с номером ячейки чехла
        case_cell_text = text(key, BLACK, WHITE, 20)
        display.blit(case_cell_text,
                (value[0] - case_cell_text.get_width() / 2, value[1] - case_cell_text.get_height() / 2))

    display.blit(axes, (0.75 * W, 0.70 * H))


def anim(display, n):
    # display.fill(WHITE)
    for i in range(n):
        pos_i = load_schedule[i][0] # Взятие координаты очередной ячейки в системе хх-хх по порядку загрузки
        coord_i = az_coords[pos_i] # Взятие координаты очередной ячейки в декартовой плоскости
        tmp_text = az_data[pos_i] # Взятие информации о ТВС/СУЗ в очердной ячейке
        color_bg = colors[tmp_text[2]]  # Взятие цвета ячейки в соответствии с номером чехла

        res = text_box(tmp_text[0], tmp_text[1], BLACK, color_bg, 22)
        draw_hex_area(display, color_bg, BLACK, radius, coord_i, 1)
        display.blit(res, (coord_i[0] - res.get_width() / 2, coord_i[1] - res.get_height() / 2))

        step = text(str(i+1), BLACK, WHITE, 70, True)
        display.blit(step, (0.75 * W, 0.70 * H))
