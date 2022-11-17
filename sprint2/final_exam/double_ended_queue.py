# id посылки 75157426
from typing import List


class DoubleEndedQueue:
    '''Дэк, который позволяет и добавлять, и извлекать элементы с обоих концов.'''

    def __init__(self, max_size) -> None:
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head_front = 0
        self.head_back = 0
        self.tail_front = 0
        self.tail_back = 0
        self.size_queue = 0

    def is_empty(self):
        '''Определяет, пуста ли очередь'''

        return self.size_queue == 0

    def push_front(self, x):
        '''Добавляет число x в начало очереди.'''

        if self.size_queue != self.max_size:
            if self.size_queue == 0:
                self.queue[self.tail_back] = x
                self.tail_back = (self.tail_back + 1) % self.max_size
                self.tail_front = (self.tail_front - 1) % self.max_size
            else:
                self.queue[self.tail_back] = x
                self.head_front = self.tail_back
                self.tail_back = (self.tail_back + 1) % self.max_size
            self.size_queue += 1
        else:
            print('error')

    def push_back(self, x):
        '''Добавляет число x в конец очереди.'''

        if self.size_queue != self.max_size:
            if self.size_queue == 0:
                self.queue[self.tail_front] = x
                self.tail_front = (self.tail_front - 1) % self.max_size
                self.tail_back = (self.tail_back + 1) % self.max_size
            else:
                self.queue[self.tail_front] = x
                self.head_back = self.tail_front
                self.tail_front = (self.tail_front - 1) % self.max_size
            self.size_queue += 1
        else:
            print('error')

    def pop_front(self):
        '''Удаляет число из начала очереди и выводит на печать.'''

        if self.is_empty():
            return print('error')
        print(self.queue[self.head_front])
        x = self.queue[self.head_front] = None
        self.size_queue -= 1
        if self.size_queue == 0:
            self.head_back = self.head_front = self.tail_back = self.tail_front = 0
            return x
        self.head_front = (self.head_front - 1) % self.max_size
        self.tail_back = (self.tail_back - 1) % self.max_size
        return x

    def pop_back(self):
        '''Удаляет число с конца очереди и выводит на печать.'''

        if self.is_empty():
            return print('error')
        print(self.queue[self.head_back])
        x = self.queue[self.head_back] = None
        self.size_queue -= 1
        if self.size_queue == 0:
            self.head_back = self.head_front = self.tail_back = self.tail_front = 0
            return x
        self.head_back = (self.head_back + 1) % self.max_size
        self.tail_front = (self.tail_front + 1) % self.max_size
        return x


def read_input() -> List[str]:
    '''Считывает входные данные.'''

    number_of_commands = int(input())
    max_size_queue = int(input())
    commands = [list(map(str, input().split()))
                for i in range(number_of_commands)]
    return number_of_commands, max_size_queue, commands


if __name__ == '__main__':
    number_of_commands, max_size_queue, commands = read_input()
    queue = DoubleEndedQueue(max_size_queue)
    for command in commands:
        if command[0] == 'push_front':
            queue.push_front(int(command[1]))
        if command[0] == 'push_back':
            queue.push_back(int(command[1]))
        if command[0] == 'pop_front':
            queue.pop_front()
        if command[0] == 'pop_back':
            queue.pop_back()
