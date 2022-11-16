from typing import List


class StackMaxEffective():
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if len(self.max_items) == 0:
            return self.max_items.append(item)
        if item > self.max_items[-1]:
            max_item = item
        else:
            max_item = self.max_items[-1]
        self.max_items.append(max_item)

    def pop(self):
        if self.items:
            self.items.pop()
            self.max_items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(self.max_items[-1])
        else:
            print('None')


def read_input() -> List[str]:
    n = int(input())
    commands = [list(map(str, input().split())) for i in range(n)]
    return commands


if __name__ == '__main__':
    commands = read_input()
    stack = StackMaxEffective()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()
