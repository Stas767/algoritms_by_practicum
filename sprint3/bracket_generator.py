def read_input() -> int:
    '''Считывает и возвращает кол-во возможных
    скобочных последовательностей ( и ).
    '''

    n = int(input())
    return n


def gen_binary(n: int, open_br: int = 0, close_br: int = 0, prefix: str = '') -> None:
    '''Печатает все возможные скобочные последовательности заданной длины n,
    в алфавитном '( ' и ')' порядке.
    '''

    if n * 2 == len(prefix):
        print(prefix)
        return
    if open_br < n:
        gen_binary(n, open_br + 1, close_br, prefix + '(')
    if close_br < open_br:
        gen_binary(n, open_br, close_br + 1,  prefix + ')')


def main() -> None:
    n=read_input()
    gen_binary(n)


if __name__ == '__main__':
    main()
