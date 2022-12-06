from dataclasses import dataclass
import random
from typing import List, Tuple


@dataclass
class Player:
    '''Класс с участниками соревнований.'''

    name: str
    score: int
    penalty: int

    def __lt__(self, other: 'Player'):
        if not isinstance(other, Player):
            raise TypeError(
                'Сравнивать можно только с объектом класса Player.')
        return (-self.score, self.penalty, self.name) < (-other.score, other.penalty, other.name)

    def __str__(self):
        return self.name


def read_input() -> List[Player]:
    '''Считывает входящие данные, создает экземпляр класса и возвращает список.'''

    count_line = int(input())
    array = []
    for _ in range(count_line):
        line = input().split()
        player = Player(
            line[0],
            int(line[1]),
            int(line[2])
        )
        array.append(player)
    return array


def partition(array: List[Player], pivot: Player, left: int, right: int) -> List[int]:
    '''in-place quick sort.'''

    i, j = left, right

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return i, j


def quicksort(array: List[Player], left: int = 0, right: int = None) -> None:
    '''Сортировка Хоара без использования дополнительной памяти для создания списков слияния.'''

    if right is None:
        right = len(array) - 1
    if len(array) < 2:
        return array
    if left >= right:
        return
    else:
        pivot = array[random.randint(left, right)]
        i, j = partition(array, pivot, left, right)
        quicksort(array, left, j)
        quicksort(array, i, right)


def main() -> None:
    '''Основная логика программы.'''
    
    array = read_input()
    quicksort(array)
    for player in array:
        print(player)


if __name__ == '__main__':
    main()
