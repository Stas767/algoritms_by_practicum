# id посылки 75206565
from typing import List


def get_polish_notation_result(polish_notation_list: List[str]) -> int:
    '''Возвращает результат выражения с обратной польской нотацией.'''

    stack = []
    for value in polish_notation_list:
        if value.isdigit() or value[1:].isdigit():
            stack.append(int(value))
        if value == '+':
            values_sum = stack.pop() + stack.pop()
            stack.append(values_sum)
        if value == '-':
            values_diff = stack.pop(-2) - stack.pop()
            stack.append(values_diff)
        if value == '*':
            values_product = stack.pop() * stack.pop()
            stack.append(values_product)
        if value == '/':
            values_quotient = stack.pop(-2) // stack.pop()
            stack.append(values_quotient)

    return stack[-1]


def read_input() -> List[str]:
    '''Считывет и возвращает входные данные.'''
    enter_list = list(input().split())
    return enter_list


if __name__ == '__main__':
    polish_notation_list = read_input()
    print(get_polish_notation_result(polish_notation_list))
