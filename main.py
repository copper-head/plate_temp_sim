# ADD FEATURE WHERE TEMPERATURE CAN BE ADDED LIVE

import numpy
import random
import copy
import pygame
from math_functions import *
from colour import Color

# Window dimensions
WIDTH = 640
HEIGHT = 480

GRID_SIZE = 100

temp_range = (50, 250)

# Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plate Temp Simulation v0.0.1")

# Tick rate of the clock
TICK_RATE = 1000

# Conductivity of the plate
conductivity = 0.1

# Color Gradient
red = Color("red")
org_colors = list(red.range_to(Color("blue"), temp_range[1] - temp_range[0]))
org_colors.reverse()
colors = []


for i in range(len(org_colors)):
    color_code = org_colors[i].get_rgb()

    color_list = []
    for i in range(3):
        color_code_final = int(color_code[i] * 255)
        color_list.append(color_code_final)

    color_tup = (color_list[0], color_list[1], color_list[2])

    colors.append(color_tup)

plate = [[float(random.randint(1, 100)) for temp in range(GRID_SIZE)] for point in range(GRID_SIZE)]



def shape_plate(shape="metaball", count=1):

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            plate[i][j] = 0

    for k in range(count):
        x, y = random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)
        scale = random.randint(1000, 3000)
        size = random.randint(1, 10)

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):

                if shape == "metaball":
                    plate[i][j] += metaball_function_2d((i, j), (x, y), scale, temp_range[1])

                if shape == "normal_dist":
                    plate[i][j] += normal_dist_3d((i, j), (x, y), scale, temp_range[1], size)

                if shape == "random":
                    height = float(random.randint(temp_range[0], temp_range[1]))
                    plate[i][j] += height

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):

                if plate[i][j] > temp_range[1]:
                    plate[i][j] = temp_range[1]

                if plate[i][j] < temp_range[0]:
                    plate[i][j] = temp_range[0] + 3




shape_plate(shape="normal_dist", count=80)

print(plate)

display_plate = copy.deepcopy(plate)

class TempPoint:

    '''

    Defines a point on the screen that represents a temp point

    parameters:
        x_pos -- x position of the temperature point
        y_pos -- y position of the temperature point
        temp -- initial temperature of the point

    '''

    def __init__(self, x_pos: int, y_pos: int, temp: float):

        self.color = colors[int(temp - 1) - temp_range[0]]
        self.rect = pygame.Rect(x_pos, y_pos, 4, 4)
        self.obj = pygame.draw.rect(window, self.color, self.rect)
        self.temp = temp

    def update_temp(self, temp):
        self.temp = temp
        self.color = colors[int(temp - 1) - temp_range[0]]

    def draw_point(self):
        self.obj = pygame.draw.rect(window, self.color, self.rect)

rect_plate = [[TempPoint(0, 0, float(random.randint(50, 100))) for temp in range(GRID_SIZE)] for point in range(GRID_SIZE)]

for i in range(len(rect_plate)):
    for j in range(len(rect_plate[i])):
        rect_plate[i][j].rect.x = j * 4 + WIDTH//2 - 2*GRID_SIZE
        rect_plate[i][j].rect.y = i * 4 + HEIGHT//2 - 2*GRID_SIZE

def draw_window():
    window.fill((0, 0, 0))
    for row in rect_plate:
        for point in row:
            point.draw_point()
    pygame.display.update()

run = True
clock = pygame.time.Clock()

runtime = 0
while run:

    # Compute Next Plate Temps
    plate_copy = copy.deepcopy(plate)
    temp_sum = 0
    for i in range(len(plate)):
        for j in range(len(plate[i])):

            temp_sum += plate_copy[i][j]

            if i != 0:
                change_1 = plate_copy[i - 1][j] - plate_copy[i][j]
            else:
                change_1 = 0

            if j != 0:
                change_2 = plate_copy[i][j - 1] - plate_copy[i][j]
            else:
                change_2 = 0

            if i != len(plate) - 1:
                change_3 = plate_copy[i + 1][j] - plate_copy[i][j]
            else:
                change_3 = 0

            if j != len(plate) - 1:
                change_4 = plate_copy[i][j + 1] - plate_copy[i][j]
            else:
                change_4 = 0

            plate[i][j] += conductivity * (change_1 + change_2 + change_3 + change_4)

            rect_plate[i][j].update_temp(plate[i][j])


    # ----------- Pygame and Drawing Stuff ----------- #

    clock.tick(TICK_RATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #if runtime % 10 == 0:
    draw_window()


    runtime += 1
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

    for row in display_plate:
        print(row)

    print(temp_sum)
    '''
