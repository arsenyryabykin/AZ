from shelf_coords import shelf_coords
from Cell import Cell
from config import radius
from shelf_content import get_shelf

def make_shelf(screen, shelf_number):
    shelf_cells = []
    shelf = get_shelf(shelf_number)

    for key, value in shelf_coords.items():
        id = key
        position = value
        tvs_text = shelf[key]
        shelf_cells.append(Cell(screen, id, radius, position, tvs_text))

    return shelf_cells


