# Advent of Code 2024
# Author: Przemysław Graczyk

import numpy as np

def load(path):
    try:
        with open(path, 'r') as file:
            array = np.array([list(line.strip()) for line in file], dtype=str)
        print(f"Loaded array with shape: {array.shape}")
        return array
    except IOError:
        print("Error: File not found or can't be read.")
        return None

def find_word_neighbors(grid, target_word: str):
    if grid is None:
        return 0
    
    match_count = 0
    num_rows, num_cols = grid.shape
    directions = [
        (-1,  0),
        (1,   0),
        (0,  -1),
        (0,   1),
        (-1, -1),
        (-1,  1),
        (1,  -1),
        (1,   1),
    ]
    word_length = len(target_word)

    def in_bounds(row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols

    def search_direction(start_row, start_col, delta_row, delta_col):
        for index in range(word_length):
            new_row = start_row + index * delta_row
            new_col = start_col + index * delta_col
            if not in_bounds(new_row, new_col) or grid[new_row, new_col] != target_word[index]:
                return False
        return True

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row, col] == target_word[0]:
                for delta_row, delta_col in directions:
                    if search_direction(row, col, delta_row, delta_col):
                        match_count += 1
    return match_count

def find_word_neighbors_x_shape(grid):
    rows, cols = grid.shape
    match_count = 0

    def check_x_shape(grid, row, col):
        
        rows, cols = grid.shape

        if row - 1 < 0 or row + 1 >= rows or col - 1 < 0 or col + 1 >= cols:
            return False

        patterns = ["MAS", "SAM"]

        l_diag = "".join([grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1]])
        r_diag = "".join([grid[row - 1][col + 1], grid[row][col], grid[row + 1][col - 1]])

        if (l_diag in patterns and r_diag in patterns) or (
            l_diag[::-1] in patterns and r_diag[::-1] in patterns
        ):
            return True

        return False
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if check_x_shape(grid, i, j):
                match_count += 1
    return match_count 

if __name__ == '__main__':
    data = load("data/day_04.txt")
    xmas_count = find_word_neighbors(grid=data, target_word='XMAS')
    x_mas_count = find_word_neighbors_x_shape(grid=data)
    print(f"'XMAS' found {xmas_count} times")
    print(f"'X-MAS' found {x_mas_count} times")
