enter_list = [95431, 57235, 43189, 89303, -21843, -97712, 97353, 69414, -68429, 93363, -
              65350, 26017, 26834, -35526, -28145, 6915, 52972, 11065, 50177, -80813, 18476, -83252]
find_el = 26017

def find_element(enter_list, find_el):
    '''Линейный поиск.'''
    
    for i in range(len(enter_list)):
        if enter_list[i] == find_el:
            return i

    return -1

print(find_element(enter_list, find_el))