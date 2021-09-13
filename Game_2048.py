import numpy as np


class Game_2048():

    def __init__(self, size=4, target=2048):
        self.target = target
        self.score = 0
        self.cur_maxvalue = 0
        self.size = size
        self.board = np.zeros((size, size), dtype=np.int32)

        self.random_add_number()  # initialize the board

        self.rotations = {"l": 0, "u": 1, "r": 2, "d": 3}

    def random_add_number(self):
        new_number = np.randome.choice([2, 4])
        cell_candidate = np.argwhere(self.board == 0)  # get cells that are empty
        location = cell_candidate[np.random.randint(0, len(cell_candidate))]
        self.board[location] = new_number

    def update_board(self, motion):
        self.board = np.rot90(self.board, self.rotations[motion])
        for i, row in enumerate(self.board):
            self.board[i] = self.row_update(row)
        self.board = np.rot90(self.board, -self.rotations[motion])

    def row_update(self, row):
        new_row = np.zeros_like(row)
        cur = 0
        for cell in row:
            if cell == 0:
                continue
            if new_row[cur] == 0:
                new_row[cur] = cell
            elif new_row[cur] == cell:
                new_row[cur] += cell
                cur += 1
            else:
                cur += 1
                new_row[cur] = cell
        return new_row

# assert motion is legal

# vertical motion


def foo(word):
    p_a = 0.45
    ls = []
    last = 1
    for l in word:
        if not ls:
            if l == 'a':
                ls.append(1 - p_a)
                last = p_a
            elif l == 'b':
                ls.append(p_a)
                last = 1 - p_a
        else:
            prev = ls[-1] * last / (1-last)
            if l == 'a':
                ls.append(prev * (1 - p_a))
                last = p_a
            elif l == 'b':
                ls.append(prev * p_a)
                last = 1 - p_a
    prev = ls[-1] * last / (1 - last)
    numerator = len(word) * prev
    denominator = 1
    for i, n in enumerate(ls):
        numerator += (i+1) * n
        denominator -= n
    return np.ceil(numerator / denominator)

print(foo('abab'))