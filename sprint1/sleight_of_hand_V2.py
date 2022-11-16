# ID посылки 74754119
from typing import Tuple


def get_score(k: int, matrix: str) -> int:
    """Получает на вход строку и целое число.
    Циклом от 1 до 9(возможный диапозон строки) проверяет
    наличие элементов в матрице и считает их кол-во.
    Если сумма больше числа k, добавляет 0 очков.
    Если меньше или равно добавляет 1 очко.
    Возвращает счет.
    """
    score = 0
    list_sum = [0] * 10
    for i in matrix:
        if i != '.':
            list_sum[int(i)] += 1

    for sum in list_sum:
        if sum != 0:
            if sum <= k:
                score += 1

    return score


def read_input() -> Tuple[int, str]:
    k = int(input()) * 2
    matrix = ''
    matrix = ''.join(matrix + input() for i in range(4))
    return k, matrix

def main():
    k, matrix = read_input()
    print(get_score(k, matrix))

if __name__ == '__main__':
    import timeit
    main()
    print(timeit.timeit("get_score(k, matrix)", setup="from __main__ import get_score"))
