def get_fibonacci_n(num) -> int:
    '''Реурсивно находит число Фибоначчи и возвращает его.'''

    if num == 0 or num == 1:
        return 1
    return get_fibonacci_n(num - 1) + get_fibonacci_n(num - 2)


def read_input() -> int:
    '''Считывает и возвращает входящие данные.'''

    num = int(input())
    return num


def main() -> None:
    '''Логика алгоритма.'''

    num = read_input()
    result = get_fibonacci_n(num)
    print(result)


if __name__ == '__main__':
    main()
