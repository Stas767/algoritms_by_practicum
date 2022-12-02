

from typing import List, Tuple


def less(number1: str, number2: str) -> bool:
    '''Сравнивает две возможные последовательности.'''
    
    if int(number1 + number2) > int(number2 + number1):
        return True
    return False


def insertion_sort_by_compare(count_n, array):
    '''Сортировка вставками с использованием компаратора.
    Находит наибольшее возможное счисло из входящих последовательностей чисел.
    '''

    for i in range(1, count_n):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


def read_input() -> Tuple[int, List[int]]:
    '''Считывает и возвращает входные данные.'''

    count_n = int(input())
    array = input().strip().split()

    return count_n, array


def main():
    count_n, array = read_input()
    insertion_sort_by_compare(count_n, array)
    print(*array, sep='')


if __name__ == '__main__':
    main()
