from shelf_coords import shelf_coords
from Cell import Cell
from config import radius

def make_shelf(screen):
    shelf = []

    # Получить данные по координатам и ТВС из БД, словарь вида {Координата ячейки МТ : (ТВС, СУЗ)}
    #az_data = get_az_data()

    for key, value in shelf_coords.items():
        id = key
        position = value
        shelf.append(Cell(screen, id, radius, position, ("N00536И1", "N0644И6")))

    return shelf
