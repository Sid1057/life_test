class Cell:
    'Class describe alived cell if it does exist.'

    def __init__(self, x, y, sort=None):
        'Simple constructor'
        self.__x = x
        self.__y = y
        self.sort = sort

    def get_coords(self):
        'Coordinates getter'
        return self.__x, self.__y

    def get_neighbours(self):
        'List of neighbours getter'
        x, y = self.__x, self.__y
        return [Cell(i[0], i[1]) for i in (
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1))]

    def __eq__(self, other):
        'Magic method for using this class as operand of `equal` method'
        if isinstance(other, type(self)):
            return self.get_coords() == other.get_coords()

        return False

    def __hash__(self):
        'Magic method for using this class as set element'
        return hash((1+self.__x) ** (1+abs(self.__y) ** (1 + self.__y < 0)))

    def __str__(self):
        'Magic method for string representation'
        return '<{}; {}>'.format(self.__x, self.__y)

    def __repr__(self):
        'Magic method for pretty printing'
        return self.__str__()
from modules.cell import Cell
from modules.world import World

import cv2 as cv
import numpy as np


def nothing(x):
    pass


class Gui:
    def __init__(self, grid_size=50, width=600, height=600):
        cv.namedWindow('field')

        self.__grid_size = grid_size
        self.__width = width
        self.__height = height

        # cv.createTrackbar('shift_x', 'params', 0, 500, nothing)
        # cv.createTrackbar('shift_y', 'params', 0, 500, nothing)
        # cv.createTrackbar('max_x', 'params', 0, 500, nothing)
        # cv.createTrackbar('max_y', 'params', 0, 500, nothing)
        # cv.createTrackbar('grid_size', 'params', 0, 50, nothing)

    def set_args(self,
            shift_x,
            shift_y,
            max_x,
            max_y,
            root_x=0,
            root_y=0):
        self.user_grid_size = 10
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.max_x = max_x
        self.max_y = max_y
        self.root_x = root_x
        self.root_y = root_y

    def draw(self, world):
        assert isinstance(world, World)

        alived = world.get_cells()
        user_grid_size = 10
        shift_x = self.shift_x
        shift_y = self.shift_y
        max_x = self.max_x
        max_y = self.max_y

        self.__grid_size = user_grid_size
        self.__height = self.__grid_size * max_y
        self.__width = self.__grid_size * max_x
        field = np.ones(
            (self.__height, self.__width, 3), dtype=np.uint8) * 255

        print(self.__height)
        for y in range(0, self.__height, self.__grid_size):
            for x in range(0, self.__width, self.__grid_size):
                x += shift_x
                y += shift_y

                field = cv.line(field, (x, 0), (x, self.__height), 0)
                color = (0, 0, 0)
                if Cell(x/self.__grid_size+self.root_x, y/self.__grid_size+self.root_y) in alived:
                    for tmp_cell in alived:
                        if tmp_cell == Cell(x/self.__grid_size+self.root_x, y/self.__grid_size+self.root_y):
                            print(tmp_cell.sort)
                            if tmp_cell.sort == 'A':
                                color = (255, 0, 0)
                                break
                            if tmp_cell.sort == 'B':
                                color = (0, 0, 255)
                                break
                            if tmp_cell.sort == 'C':
                                color = (0, 255, 0)
                                break
                            if tmp_cell.sort == 'D':
                                color = (0, 0, 0)
                                break
                    field = cv.rectangle(
                        field,
                        (x-self.root_x*self.__grid_size, y-self.root_y*self.__grid_size),
                        (x+self.__grid_size-self.root_x*self.__grid_size, y+self.__grid_size - self.__grid_size*self.root_y),
                        color, cv.FILLED)

                field = cv.line(field, (0, y), (self.__width, y), 0)

        cv.imshow('field', field)
        return cv.waitKey(100)
from modules.cell import Cell


class World():
    'Class of the field of the game. Collect all alived cells.'
    def __init__(self, cells=[]):
        'Simple constructor of initial state'
        assert all(isinstance(cell, Cell) for cell in cells)
        self.__cells = cells
        World.step = 0

    def set_cells(self, cells):
        'Setter of alived cells'
        assert all(isinstance(cell, Cell) for cell in cells)
        self.__cells = set(cells)

    def get_cells(self):
        'Getter of alived cells'
        return self.__cells

    @staticmethod
    def update_stete(cells):
        'Static method of updating the state of the world'
        assert all(isinstance(cell, Cell) for cell in cells)

        # create containers of alived cells and possible alived cells
        alive_cells = cells
        neighbours = []

        # fill container of possible alived cells
        for cell in cells:
            neighbours += cell.get_neighbours()
        neighbours += [cell for cell in alive_cells]
        neighbours = {cell for cell in neighbours}

        # create container of really alived cells
        result = []

        def get_sort_neighbours_count(sort, alive_cells, neighbours):
                return sum([
                    cell in filter(lambda c: c.sort == sort, alive_cells) for\
                        cell in neighbour.get_neighbours()])

        # check every possible alived cells using Game of life rules
        for neighbour in neighbours:
            for tmp_n in alive_cells:
                if tmp_n == neighbour: neighbour = tmp_n
            local_neighbours_count_D = get_sort_neighbours_count(
                'D', alive_cells, neighbours)
            local_neighbours_count_C = get_sort_neighbours_count(
                'C', alive_cells, neighbours)
            local_neighbours_count_B = get_sort_neighbours_count(
                'B', alive_cells, neighbours)
            local_neighbours_count_A = get_sort_neighbours_count(
                'A', alive_cells, neighbours)

            if neighbour.sort is None:
                if local_neighbours_count_D == 3:
                    neighbour.sort = 'D'
                    result.append(neighbour)
                    continue

                if local_neighbours_count_C == 3:
                    neighbour.sort = 'C'
                    result.append(neighbour)
                    continue

                if local_neighbours_count_B == 3:
                    neighbour.sort = 'B'
                    result.append(neighbour)
                    continue

                if local_neighbours_count_A == 3:
                    neighbour.sort = 'A'
                    result.append(neighbour)
                    continue

            elif neighbour.sort == 'D':
                if  \
                        local_neighbours_count_D >= 2 or \
                        local_neighbours_count_C >= 2 or \
                        local_neighbours_count_B >= 2 or \
                        local_neighbours_count_A >= 2:
                    neighbour.sort = 'D'
                    result.append(neighbour)
                    continue


            elif neighbour.sort == 'C':
                if local_neighbours_count_D == 3:
                    neighbour.sort = 'D'
                    result.append(neighbour)
                    continue

                if local_neighbours_count_C > 1:
                    result.append(neighbour)
                    continue

            elif neighbour.sort == 'B':
                if local_neighbours_count_D == 3:
                    neighbour.sort = 'D'
                    result.append(neighbour)
                    continue

                if local_neighbours_count_B == 3:
                    result.append(neighbour)
                    continue
                elif neighbour in alive_cells and local_neighbours_count_B==2:
                    result.append(neighbour)
                    continue

            elif neighbour.sort == 'A':
                if local_neighbours_count_D == 3:
                    neighbour.sort = 'D'
                    result.append(neighbour)
                    continue

                if World.step % 2 == 0:
                    result.append(neighbour)
                    continue
                if local_neighbours_count_A == 3:
                    result.append(neighbour)
                    continue
                elif neighbour in alive_cells and local_neighbours_count_A==2:
                    result.append(neighbour)
                    continue

        # return alived cells as a set
        return {cell for cell in result}

    def next_state(self):
        'Method of evaluating the game\'s state'
        print('\nPrev. state:   {}'.format(self.__cells))
        World.step += 1
        self.__cells = self.update_stete(self.__cells)
        print('Current state: {}\n'.format(self.__cells))
#!/usr/bin/python3

from modules.cell import Cell
from modules.world import World
from modules.gui import Gui
import numpy as np
import tkinter as tk
import PIL
import PIL.Image, PIL.ImageTk
import cv2 as cv

world = World(
    {
        Cell(0, 0, 'B'),
        Cell(1, 1, 'B'),
        Cell(1, 2, 'B'),
        Cell(0, 2, 'B'),
        Cell(-1, 2, 'B'),

        Cell(4, 5, 'C'),
        Cell(4, 4, 'C'),
        Cell(2, 4, 'C'),
        Cell(3, 4, 'C'),

        Cell(-1, -1, 'A'),
        Cell(-2, -1, 'A'),
        Cell(0, -1, 'A'),

        Cell(-3, -1, 'D'),
        Cell(-4, -1, 'D'),
        Cell(-5, -1, 'D'),
        Cell(-6, -1, 'D'),

        # Cell(-0, -5, 'A'),
        # Cell(-7, -1, 'A'),
        })
gui = Gui(20)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        self.field = np.zeros((400, 400, 3), dtype=np.uint8)
        height, width, channels = self.field.shape

        # interface
        self.frame2=tk.Frame(self,width=200,height=400)
        self.frame2.grid(row=0, column=1)

        # ширина поляв клетках
        self.textX1=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textX1.place(x='0', y='0')
        self.labelX1=tk.Label(self.frame2,text='X1',font='Arial 14')
        self.labelX1.place(x='170', y='0')

        # высота поляв клетках
        self.textY1=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textY1.place(x='0', y='50')
        self.labelY1=tk.Label(self.frame2,text='Y1',font='Arial 14')
        self.labelY1.place(x='170', y='50')

        # смещение по горизонтали
        self.textX2=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textX2.place(x='0', y='100')
        self.labelX2=tk.Label(self.frame2,text='X2',font='Arial 14')
        self.labelX2.place(x='170', y='100')

        # смещение по вертикали
        self.textY2=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textY2.place(x='0', y='150')
        self.labelY2=tk.Label(self.frame2,text='Y2',font='Arial 14')
        self.labelY2.place(x='170', y='150')

        self.quit = tk.Button(
            self.frame2, text='next', fg="red", width='22',
            command=self.say_hi)
        self.quit.place(x='0', y='350')

    def say_hi(self):
        print("hi there, everyone!")
        root.update()
        max_x = int(self.textX1.get())
        max_y = int(self.textY1.get())
        root_x = int(self.textX2.get())
        root_y = int(self.textY2.get())

        gui.set_args(10, 10, max_x, max_y, root_x, root_y)
        gui.draw(world)
        world.next_state()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
i = 0
#while True:
#    print('step {}'.format(i))
#    key = gui.draw(world)
#
#    if key == ord('q'):
#        exit()
#
#    world.next_state()
