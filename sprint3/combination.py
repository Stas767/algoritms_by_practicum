letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def read_input() -> str:
    '''Считывает и возвращает входные данные.'''

    enter_str = input()
    return enter_str


def get_combination(enter_str: str, combination: str = ''):
    '''Печатает все комбинации букв, 
    которые можно набрать enter_str последовательностью.
    '''

    if not enter_str:
        print(combination, end=' ')
        return
    for letter in letters[enter_str[0]]:
        combination += letter
        get_combination(enter_str[1:], combination)
        combination = combination[:-1]


def main() -> None:
    '''Основная логика алгоритма.'''

    enter_str = read_input()
    get_combination(enter_str)


if __name__ == '__main__':
    main()
