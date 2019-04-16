from modules.cell import Cell


class World():
    'Class of the field of the game. Collect all alived cells.'
    def __init__(self, cells=[]):
        'Simple constructor of initial state'
        cells = set(cells)
        assert all(
            isinstance(cell, Cell) for cell in cells)
        self.__cells = cells

        World.step = 0

    def set_cells(self, cells):
        'Setter of alived cells'
        cells = set(cells)
        assert all(
            isinstance(cell, Cell) for cell in cells)

        self.__cells = set(cells)

    def get_cells(self):
        'Getter of alived cells'
        self.__cells = set(self.__cells)
        return self.__cells

    @staticmethod
    def update_stete(cells):
        'Static method of updating the state of the world'
        assert all(
            isinstance(cell, Cell) for cell in cells)

        # create containers of alived cells and possible alived cells
        alive_cells = cells
        neighbours = []

        # fill container of possible alived cells
        for cell in cells:
            neighbours += cell.get_neighbours()
        neighbours += [
            cell for cell in alive_cells]
        neighbours = {
            cell for cell in neighbours}

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
        return {
            cell for cell in result}

    def next_state(self):
        'Method of evaluating the game\'s state'
        print('\nPrev. state:   {}'.format(self.__cells))
        World.step += 1
        self.__cells = self.update_stete(self.__cells)
        print('Current state: {}\n'.format(self.__cells))
