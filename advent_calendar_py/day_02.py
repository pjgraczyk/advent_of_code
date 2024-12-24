# Advent of Code 2024
# Author: Przemysław Graczyk

import numpy as np

def extract(path):
    with open(path, "r") as file:
        return [np.array(line.replace("\n", "").split(" "), dtype=float) for line in file]  
    
def check_safety_level(array):
    if len(array) < 3:
        return True

    for i in range(2, len(array)):

        diff_1 = (
            array[i] - array[i - 1]
        )
        diff_2 = (
            array[i - 1] - array[i - 2]
        )

        if (diff_1 > 0 and diff_2 < 0) or (diff_1 < 0 and diff_2 > 0):
            return False

        if not (1 <= abs(diff_1) <= 3) or not (1 <= abs(diff_2) <= 3):
            return False

    return True

def check_safety_level_corrected(array):
    def is_safe(subarray):
        for i in range(2, len(subarray)):
            diff_1 = subarray[i] - subarray[i - 1]
            diff_2 = subarray[i - 1] - subarray[i - 2]

            if (diff_1 > 0 and diff_2 < 0) or (diff_1 < 0 and diff_2 > 0):
                return False
            
            if not (1 <= abs(diff_1) <= 3) or not (1 <= abs(diff_2) <= 3):
                return False
        return True

    if is_safe(array):
        return True

    for i in range(len(array)):
        subarray = np.delete(array, i)
        if is_safe(subarray):
            return True

    return False

if __name__ == "__main__":
    data = extract('data/day_02.txt')
    count = 0
    for array in data:
        if check_safety_level_corrected(array):
            count += 1
    print(count)
    