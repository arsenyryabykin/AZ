import math
from config import radius, case_center

# radius = 60
x0, y0 = case_center
x = 2 * radius
y = math.sqrt(3/4) * x
dx = 2.7*radius
dy = 2.2*radius

case_coords = {"1" : (x0 - 2*dx, y0 + 2*dy),
               "2" : (x0 - 1*dx, y0 + 2*dy),
               "3" : (x0, y0 + 2*dy),
               "4" : (x0 + 1*dx, y0 + 2*dy),
               "5" : (x0 + 2*dx, y0 + 2*dy),
               "6" : (x0 - 2.5*dx,y0 + 1*dy),
               "7" : (x0 - 1.5*dx,y0 + 1*dy),
               "8" : (x0 - 0.5*dx,y0 + 1*dy),
               "9" : (x0 + 0.5*dx,y0 + 1*dy),
               "10" : (x0 + 1.5*dx,y0 + 1*dy),
               "11" : (x0 + 2.5*dx,y0 + 1*dy),
               "12" : (x0 - 2*dx, y0),
               "13" : (x0 - 1*dx, y0),
               "14" : (x0, y0),
               "15" : (x0 + 1*dx, y0),
               "16" : (x0 + 2*dx, y0),
               "17": (x0 - 2.5 * dx, y0 - 1 * dy),
               "18": (x0 - 1.5 * dx, y0 - 1 * dy),
               "19": (x0 - 0.5 * dx, y0 - 1 * dy),
               "20": (x0 + 0.5 * dx, y0 - 1 * dy),
               "21": (x0 + 1.5 * dx, y0 - 1 * dy),
               "22": (x0 + 2.5 * dx, y0 - 1 * dy),
               "23": (x0 - 2 * dx, y0 - 2 * dy),
               "24": (x0 - 1 * dx, y0 - 2 * dy),
               "25": (x0, y0 - 2 * dy),
               "26": (x0 + 1 * dx, y0 - 2 * dy),
               "27": (x0 + 2 * dx, y0 - 2 * dy)}


case_cells_coords = {"1" : (x0 - 2*dx, y0 + 2*dy + 0.75*radius),
               "2" : (x0 - 1*dx, y0 + 2*dy + 0.75*radius),
               "3" : (x0, y0 + 2*dy + 0.75*radius),
               "4" : (x0 + 1*dx, y0 + 2*dy + 0.75*radius),
               "5" : (x0 + 2*dx, y0 + 2*dy + 0.75*radius),
               "6" : (x0 - 2.5*dx,y0 + 1*dy + 0.75*radius),
               "7" : (x0 - 1.5*dx,y0 + 1*dy + 0.75*radius),
               "8" : (x0 - 0.5*dx,y0 + 1*dy + 0.75*radius),
               "9" : (x0 + 0.5*dx,y0 + 1*dy + 0.75*radius),
               "10" : (x0 + 1.5*dx,y0 + 1*dy + 0.75*radius),
               "11" : (x0 + 2.5*dx,y0 + 1*dy + 0.75*radius),
               "12" : (x0 - 2*dx, y0 + 0.75*radius),
               "13" : (x0 - 1*dx, y0 + 0.75*radius),
               "14" : (x0, y0 + 0.75*radius),
               "15" : (x0 + 1*dx, y0 + 0.75*radius),
               "16" : (x0 + 2*dx, y0 + 0.75*radius),
               "17": (x0 - 2.5 * dx, y0 - 1 * dy + 0.75*radius),
               "18": (x0 - 1.5 * dx, y0 - 1 * dy + 0.75*radius),
               "19": (x0 - 0.5 * dx, y0 - 1 * dy + 0.75*radius),
               "20": (x0 + 0.5 * dx, y0 - 1 * dy + 0.75*radius),
               "21": (x0 + 1.5 * dx, y0 - 1 * dy + 0.75*radius),
               "22": (x0 + 2.5 * dx, y0 - 1 * dy + 0.75*radius),
               "23": (x0 - 2 * dx, y0 - 2 * dy + 0.75*radius),
               "24": (x0 - 1 * dx, y0 - 2 * dy + 0.75*radius),
               "25": (x0, y0 - 2 * dy + 0.75*radius),
               "26": (x0 + 1 * dx, y0 - 2 * dy + 0.75*radius),
               "27": (x0 + 2 * dx, y0 - 2 * dy + 0.75*radius)}
