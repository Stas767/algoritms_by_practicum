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
    possible_values = '123456789'
    for i in possible_values: 
        if i in matrix:
            count = matrix.count(i)
            if count <= k:
                score += 1

    return score


def read_input() -> Tuple[int, str]:
    k = int(input()) * 2
    matrix = ''
    matrix = ''.join(matrix + input() for i in range(4))
    return k, matrix


if __name__ == '__main__':
    k, matrix = read_input()
    print(get_score(k, matrix))
