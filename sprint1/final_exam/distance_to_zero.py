# ID посылки 74749114
from typing import List, Tuple


def get_distance_to_zero(houses_list: List[int], street_len: int) -> List[int]:
    '''Поиск ближайшего расстояния до 0.'''

    result = [0] * street_len  # Бронирую место для результата
    zero_index_list = [
        index for index, value in enumerate(houses_list) if value == 0
    ]  # Генерирую список с индексами всех 0 из списка полученного на входе

    for index in range(len(zero_index_list) - 1):
        zero_1, zero_2 = zero_index_list[index], zero_index_list[index + 1]
        # Рассчитываю дистанцию между нулями и нахожу мин расстояние от объекта до нуля
        for dist_to_zero in range(zero_1, zero_2):
            result[dist_to_zero] = min(
                dist_to_zero - zero_1, zero_2 - dist_to_zero
            )

    if houses_list[0] != 0:  # Нахожу расстояние от начала списка до первого нуля
        for dist_to_zero in range(zero_index_list[0] + 1):
            result[dist_to_zero] = zero_index_list[0] - dist_to_zero

    if houses_list[-1] != 0:  # Нахожу расстояние от последнего нуля и до конца списка
        for dist_to_zero in range(zero_index_list[-1], street_len):
            result[dist_to_zero] = dist_to_zero - zero_index_list[-1]

    return result


def read_input() -> Tuple[List[int], int]:
    street_len = int(input())
    houses_list = list(map(int, input().strip().split()))
    return street_len, houses_list


if __name__ == '__main__':
    street_len, houses_list = read_input()
    print(*get_distance_to_zero(houses_list, street_len), sep=' ')
    # твой вариант print(*get_distance_to_zero) не запускался,
    # т.к. он требовал список а не функцию
    # и время работы алгоритма немного выросло)
