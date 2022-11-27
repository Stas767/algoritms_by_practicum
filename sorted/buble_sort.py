from typing import List


def buble_sort(array: List[int]) -> None:
    '''Получает на вход неотсортированный список.
    Сравнивает два числа 'k' и 'k+1'. Если первое больше, 
    меняет их местами и смещется на 1 вправо.
    '''

    for i in range(1, len(array)):
        for k in range(len(array) - i):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]


buble_sort([11, 2, 9, 7, 1])
