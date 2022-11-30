from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    '''Считывает и возвращает входные данные.'''

    n = int(input())
    array = list(map(int, input().strip().split()))

    return n, array


def bubble_sort(n, array):
    '''Сортировка пузырьком. 
    После каждого прохода по массиву, 
    на котором какие-то элементы меняются местами,
    выводите его промежуточное состояние.
    '''

    printed = True  # Если массив отсортирован, ввыводит печать.
    for i in range(1, n):
        sorted = False
        for k in range(n - i):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                sorted = True

        if sorted:
            # Выводит массив после каждой иттерации сортировки.
            print(' '.join(map(str, array)))
            printed = False

    if printed:  # Выводит на печать, если входной массив отсортирован.
        print(' '.join(map(str, array)))

def main() -> None:
    n, array = read_input()
    bubble_sort(n, array)

if __name__ == '__main__':
    main()