from typing import List, Tuple


def read_input() -> Tuple[int, int, List[List[int]]]:
    '''Считывает входящие данные.'''

    row = int(input())
    col = int(input())
    matrix = [list(map(int, input().split())) for line in range(row)]
    return row, col, matrix


def trans_matrix(row: int, col: int, matrix: List[int]) -> List[List[int]]:
    '''Транспонирует и возвращает новую матрицу.'''

    trans_matrix = [[matrix[i][j] for i in range(row)] for j in range(col)]

    return trans_matrix


def print_new_matrix(col: int, new_martix: List[List[int]]) -> None:
    '''Выводит результат в том виде, который был получен на входе.'''

    for i in range(col):
        print(' '.join(map(str, new_martix[i])))


def main():
    '''Основная логика алгоритма.'''

    row, col, matrix = read_input()
    new_matrix = trans_matrix(row, col, matrix)
    print_new_matrix(col, new_matrix)


if __name__ == '__main__':
    main()
