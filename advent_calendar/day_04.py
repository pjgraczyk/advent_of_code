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

def find_word_neighbors_x_shape(grid, target_word: str):
    if grid is None:
        return 0
    
    match_count = 0
    num_rows, num_cols = grid.shape
    directions = [
        (-1, -1),
        (-1,  1),
        (1,  -1),
        (1,   1),
    ]
    word_length = len(target_word)

    def in_bounds(row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols

    def search_x_shape(center_row, center_col):
        for delta_row, delta_col in directions:
            # Check forward direction
            if all(
                in_bounds(center_row + i * delta_row, center_col + i * delta_col) and
                grid[center_row + i * delta_row, center_col + i * delta_col] == target_word[i]
                for i in range(word_length)
            ):
                return True
        return False

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row, col] == target_word[0]:
                if search_x_shape(row, col):
                    match_count += 1

    return match_count

if __name__ == '__main__':
    data = load("../data/day_04.txt")
    xmas_count = find_word_neighbors(grid=data, target_word='XMAS')
    x_mas_count = find_word_neighbors_x_shape(grid=data, target_word='MAS')
    print(f"'XMAS' found {xmas_count} times")


















    
    print(f"'X-MAS' found {x_mas_count} times")
