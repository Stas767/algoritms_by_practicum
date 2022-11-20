# id посылки 75236442
from typing import List


class Stack():
    '''Стек для хранения чисел.'''

    def __init__(self) -> None:
        self.stack = []

    def get_polish_notation_result(self, polish_notation_list: List[str]) -> int:
        '''Возвращает результат выражения с обратной польской нотацией.'''

        operations_dict = {
            '+': lambda x2, x1: x2 + x1,
            '-': lambda x2, x1: x2 - x1,
            '*': lambda x2, x1: x2 * x1,
            '/': lambda x2, x1: x2 // x1
        }
        for value in polish_notation_list:
            #  value[1:] - для отрицательных значений, проверка на число не учитывая'-'.
            if value.isdigit() or value[1:].isdigit():
                self.stack.append(int(value))
            if value in operations_dict.keys():
                x2, x1 = self.stack.pop(-2), self.stack.pop()
                self.stack.append(operations_dict[value](x2, x1))

        return self.stack[-1]


def read_input() -> List[str]:
    '''Считывет и возвращает входные данные.'''
    enter_list = list(input().split())
    return enter_list


if __name__ == '__main__':
    polish_notation_list = read_input()
    stack = Stack()
    print(stack.get_polish_notation_result(polish_notation_list))
