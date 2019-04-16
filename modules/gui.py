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
        alived = set(alived)
        user_grid_size = 10
        shift_x = self.shift_x
        shift_y = self.shift_y
        max_x = self.max_x
        max_y = self.max_y

        assert(max_x > 0)
        assert(max_y > 0)
        assert(isinstance(shift_x, int))
        assert(isinstance(shift_y, int))
        assert(isinstance(max_x, int))
        assert(isinstance(max_y, int))

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
        key = cv.waitKey(100)
        return key != ord('q')
