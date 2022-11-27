from typing import List


def insertion_sort(array: List[int]) -> None:
    '''Получает на вход неотсортированный список. 
    При переборе каждого элемента выстраивает их в порядке возростания,
    перемещая поэлементно вправо, освобождая место для вставки элемента.
    Каждую итерацию выводит на печать.
    '''

    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print(f'step: {i}, sorted: {i + 1}, elements: {array}')


insertion_sort([11, 2, 9, 7, 1])
