from typing import List


def selection_sort(array: List[int]) -> None:
    '''Получает на вход неотсортированный список.
    Сравнивает два числа 'i' и 'i+1'. Если второе больше, меняет их местами.
    После каждого перемещения выводит инфу о новых позициях элементов в списке.
    '''

    for i in range(len(array) - 1):
        for k in range(i + 1, len(array)):
            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]
                print(f'elements: {array}')


selection_sort([11, 2, 9, 7, 1])
