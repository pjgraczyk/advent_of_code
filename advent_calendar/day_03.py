import re

def load(path):
    with open(path, 'r') as file:
        data = file.read()
    return data

def find_all_muls(data):
    matches = re.findall("mul\\(\\d{1,5}\\,\\d{1,5}\\)", data, flags=re.DOTALL)
    return matches

def find_muls_with_do(data):
    matches = re.findall("(do\(\))|(don't\(\))|(mul\(\d{1,5}\,\d{1,5}\))", data)
    return matches

def clean_do_array(matches):
    return [" ".join(filter(None, t)) for t in matches]

def replace():
    pass

def multiply(mul_string):
    mul_tuple = mul_string.replace('mul','').replace('(', '').replace(')', '').split(',')
    mul = 1
    for item in mul_tuple:
        mul *= int(item)
    return mul

if __name__ == '__main__':
    data = load('data/day_03.txt')
    matches = find_all_muls(data)
    sum_all = sum([multiply(match) for match in matches])
    print(sum_all)
    matches_do = clean_do_array(find_muls_with_do(data))
    sum_do = ([match for match in matches_do])
    print(sum_do)