from az_coords import az_coords, bipr_coords
from Cell import Cell
from sqlitedb import get_az_data

from config import radius

def make_az(screen):

    az = []
    # Получить данные по координатам и ТВС из БД, словарь вида {Координата ячейки МТ : (ТВС, СУЗ)}
    az_data = get_az_data()

    for cell_coord, text_list in az_data.items():
        id = bipr_coords[cell_coord]
        position = az_coords[cell_coord]
        az.append(Cell(screen, id, radius, position, text_list))

    return az






