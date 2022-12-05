import random
from typing import List, Tuple


def read_input() -> List[Tuple[str, int, int]]:
    count_line = int(input())
    array = []
    for _ in range(count_line):
        line = input().split()
        line[1] = int(line[1])
        line[2] = int(line[2])
        array.append(line)
    return array


def partition(array: List[Tuple[str, int, int]], pivot: Tuple[str, int, int]):
    left = []
    center = []
    right = []
    for i in array:
        if i[1] > pivot[1]:
            left.append(i)
        elif i[1] < pivot[1]:
            right.append(i)
        else:
            if i[2] < pivot[2]:
                left.append(i)
            elif i[2] > pivot[2]:
                right.append(i)
            else:
                if i[0] < pivot[0]:
                    left.append(i)
                elif i[0] > pivot[0]:
                    right.append(i)
                else:
                    center.append(i)

    return left, center, right


def quicksort(array: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    '''Сортировка Хоара с использованием дополнительной памяти.'''

    if len(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[random.randint(0, len(array) - 1)]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


def main() -> None:
    array = read_input()
    sort_array = quicksort(array)
    for i in sort_array:
        print(i[0])


if __name__ == '__main__':
    main()
