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
