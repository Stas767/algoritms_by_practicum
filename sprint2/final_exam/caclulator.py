# id посылки 75236442
# Переписал основательно =) хотя ты просил просто добавить вызов функции в словарь)
# Убрал 8 строчек if'ов и добавил еще больше ) Скажи, если это было лишним.
from typing import List


class Stack():
    '''Стек для хранения чисел.'''

    def __init__(self) -> None:
        self.stack = []

    def get_values_sum(self):
        return self.stack.pop() + self.stack.pop()

    def get_values_diff(self):
        return self.stack.pop(-2) - self.stack.pop()

    def get_values_product(self):
        return self.stack.pop() * self.stack.pop()

    def get_values_quotient(self):
        return self.stack.pop(-2) // self.stack.pop()

    def get_polish_notation_result(self, polish_notation_list: List[str]) -> int:
        '''Возвращает результат выражения с обратной польской нотацией.'''

        operations_dict = {
            '+': self.get_values_sum,
            '-': self.get_values_diff,
            '*': self.get_values_product,
            '/': self.get_values_quotient
        }
        for value in polish_notation_list:
            #  value[1:] - для отрицательных значений, проверка на число не учитывая'-'.
            if value.isdigit() or value[1:].isdigit():
                self.stack.append(int(value))
            if value in operations_dict.keys():
                self.stack.append(operations_dict[value]())

        return self.stack[-1]


def read_input() -> List[str]:
    '''Считывет и возвращает входные данные.'''
    enter_list = list(input().split())
    return enter_list


if __name__ == '__main__':
    polish_notation_list = read_input()
    stack = Stack()
    print(stack.get_polish_notation_result(polish_notation_list))
