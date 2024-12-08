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

def find_word_neighbors_x_shape(grid, target_word: str):
    if grid is None:
        return 0
    
    match_count = 0
    num_rows, num_cols = grid.shape
    word_length = len(target_word)

    directions = [
        (-1, -1),  # Up-Left
        (-1,  1),  # Up-Right
        (1,  -1),  # Down-Left
        (1,   1)   # Down-Right
    ]

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
            # Check backward direction
            if all(
                in_bounds(center_row + i * delta_row, center_col + i * delta_col) and
                grid[center_row + i * delta_row, center_col + i * delta_col] == target_word[-i - 1]
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
    xmas_count = find_word_neighbors_x_shape(grid=data, target_word='XMAS')
    print(f"'XMAS' forming an X-shape found {xmas_count} times")
