def get_fibonacci_n(n, k) -> int:
    '''Фибоначчи по модулю. 
    Выводит последние 'k' цифр числа Фибоначчи, если в искомом числе меньше k цифр,
    то выводит само число без ведущих нулей.
    '''

    num_1, num_2 = 1, 1
    dif = (10 ** k)

    if n in (0, 1):
        return 1
    for _ in range(n - 1):
        num_1, num_2 = num_2, (num_2 + num_1) % dif

    return num_2


def read_input() -> int:
    '''Считывает и возвращает входящие данные.'''

    n, k = (int(i) for i in input().split())

    return n, k


def main() -> None:
    '''Логика алгоритма.'''

    n, k = read_input()
    result = get_fibonacci_n(n, k)
    print(result)


if __name__ == '__main__':
    main()
