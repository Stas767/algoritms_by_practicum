from typing import List


class MyQueueSized:
    '''Принимает параметр max_size, означающий максимально
    допустимое количество элементов в очереди.
    '''

    def __init__(self, max_size) -> None:
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_queue = 0

    def is_empty(self):
        '''Определяет, пуста ли очередь'''
        return self.size_queue == 0

    def push(self, x):
        '''Добавляет число x в очередь.'''
        if self.size_queue != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size_queue += 1
        else:
            print('error')

    def pop(self):
        '''Удаляет число из очереди и выводит на печать.'''
        if self.is_empty():
            return print(None)
        print(self.queue[self.head])
        x = self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_queue -= 1
        return x

    def peek(self):
        '''Печатает первое число в очереди'''
        if self.is_empty():
            return print(None)
        x = self.queue[self.head]
        print(x)
        return x

    def size(self):
        '''Возвращает размер очереди'''
        print(self.size_queue)


def read_input() -> List[str]:
    number_of_commands = int(input())
    max_size_queue = int(input())
    commands = [list(map(str, input().split()))
                for i in range(number_of_commands)]
    return number_of_commands, max_size_queue, commands


if __name__ == '__main__':
    number_of_commands, max_size_queue, commands = read_input()
    queue = MyQueueSized(max_size_queue)
    for command in commands:
        if command[0] == 'push':
            queue.push(int(command[1]))
        if command[0] == 'pop':
            queue.pop()
        if command[0] == 'peek':
            queue.peek()
        if command[0] == 'size':
            queue.size()
