# 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 
#
# matrix = [[(0,0), (0,1), (0,2)],
#           [(1,0), (1,1), (1,2)],
#           [(2,0), (2,1), (2,2)]]


LIVE = 1
DEAD = 0

SMALL_POPULATION = 2
BIG_POPULATION = 3

def is_cell_living(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return DEAD

    return matrix[x][y]


def check_neighbors(matrix, x, y):
    living_cells_count = is_cell_living(matrix, x + 1, y + 1) + is_cell_living(matrix, x + 1, y) + is_cell_living(matrix, x, y + 1) + is_cell_living(matrix, x - 1, y - 1) + is_cell_living(matrix, x - 1, y) + is_cell_living(matrix, x, y - 1) + is_cell_living(matrix, x - 1, y + 1) + is_cell_living(matrix, x - 1, y + 1)

    if not is_cell_living(matrix, x, y) and living_cells_count == BIG_POPULATION:
        return LIVE

    if is_cell_living(matrix, x, y):
        if living_cells_count < SMALL_POPULATION:
            return DEAD
        if living_cells_count >= SMALL_POPULATION and living_cells_count <= BIG_POPULATION:
            return LIVE
        if living_cells_count > BIG_POPULATION:
            return DEAD

    return DEAD


def lives_search(matrix):
    vertical_size = len(matrix)
    horizontal_size = len(matrix[0])
    resultant_matrix = []

    for x in range(horizontal_size):
        resultant_matrix.append([])
        for y in range(vertical_size):
            resultant_matrix[x].append(check_neighbors(matrix, x, y))
    return resultant_matrix


def print_matrix(matrix):
    for line in matrix:
        print(line)



import unittest

class TestCheckNeighbors(unittest.TestCase):

    def test_live_cell_with_fewer_than_two_live_neighbors_dies(self):
        matrix = [[1, 1],
                  [0, 0]]
        self.assertTrue(check_neighbors(matrix, 0, 0) == 0)

    def test_live_cell_with_two__live_neighbors_lives(self):
        matrix = [[1, 1],
                  [0, 1]]
        self.assertTrue(check_neighbors(matrix, 0, 0) == 1)


    def test_live_cell_with_three_live_neighbors_lives(self):
        matrix = [[1, 1],
                  [1, 1]]
        self.assertTrue(check_neighbors(matrix, 0, 0) == 1)


    def test_live_cell_with_more_than_three_live_neighbors_dies(self):
        matrix = [[1, 1, 1],
                  [0, 1, 1],
                  [0, 0, 0]]
        self.assertTrue(check_neighbors(matrix, 1, 1) == 0)


    def test_dead_cell_with_exactly_three_live_neighbors(self):
        matrix = [[1, 0, 1],
                  [0, 0, 0],
                  [1, 0, 0]]
        self.assertTrue(check_neighbors(matrix, 1, 1) == 1)




if __name__ == "__main__":
    matrix = [[1, 1, 1],
              [0, 0, 0],
              [1, 1, 1]]


    for attempt in range(10):
        print('attempt #{0}'.format(attempt))
        matrix = lives_search(matrix)
        print_matrix(matrix)
