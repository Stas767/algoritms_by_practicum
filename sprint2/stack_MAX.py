from typing import List


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


def read_input() -> List[str]:
    n = int(input())
    commands = [list(map(str, input().split())) for i in range(n)]
    return commands


if __name__ == '__main__':
    commands = read_input()
    stack = StackMax()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()
