# id посылки 75512857
from typing import List


class DequeOverFlowError(Exception):
    """Переполнение очереди."""
    pass


class RuntimeError(Exception):
    '''Очередь пуста.'''
    pass


class Deque:
    '''Дэк, который позволяет и добавлять, и извлекать элементы с обоих концов.'''

    def __init__(self, max_size) -> None:
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head_front = 0
        self.__head_back = 0
        self.__tail_front = 0
        self.__tail_back = 0
        self.__size_queue = 0

    def is_empty(self) -> bool:
        '''Определяет, пуста ли очередь'''

        return self.__size_queue == 0

    def push_front(self, x) -> None:
        '''Добавляет число x в начало очереди.'''

        if self.__size_queue != self.__max_size:
            if self.__size_queue == 0:
                self.__queue[self.__tail_back] = x
                self.__tail_back = (self.__tail_back + 1) % self.__max_size
                self.__tail_front = (self.__tail_front - 1) % self.__max_size
            else:
                self.__queue[self.__tail_back] = x
                self.__head_front = self.__tail_back
                self.__tail_back = (self.__tail_back + 1) % self.__max_size
            self.__size_queue += 1
        else:
            raise DequeOverFlowError('error')

    def push_back(self, x) -> None:
        '''Добавляет число x в конец очереди.'''

        if self.__size_queue != self.__max_size:
            if self.__size_queue == 0:
                self.__queue[self.__tail_front] = x
                self.__tail_front = (self.__tail_front - 1) % self.__max_size
                self.__tail_back = (self.__tail_back + 1) % self.__max_size
            else:
                self.__queue[self.__tail_front] = x
                self.__head_back = self.__tail_front
                self.__tail_front = (self.__tail_front - 1) % self.__max_size
            self.__size_queue += 1
        else:
            raise DequeOverFlowError('error')

    def pop_front(self) -> int:
        '''Удаляет число из начала очереди и выводит на печать.'''

        if self.is_empty():
            raise RuntimeError('error')

        x = self.__queue[self.__head_front]
        self.__queue[self.__head_front] = None
        self.__size_queue -= 1
        if self.__size_queue == 0:
            self.__head_back = self.__head_front = self.__tail_back = self.__tail_front = 0
            return x
        self.__head_front = (self.__head_front - 1) % self.__max_size
        self.__tail_back = (self.__tail_back - 1) % self.__max_size
        return x

    def pop_back(self) -> int:
        '''Удаляет число с конца очереди и выводит на печать.'''

        if self.is_empty():
            raise RuntimeError('error')

        x = self.__queue[self.__head_back]
        self.__queue[self.__head_back] = None
        self.__size_queue -= 1
        if self.__size_queue == 0:
            self.__head_back = self.__head_front = self.__tail_back = self.__tail_front = 0
            return x
        self.__head_back = (self.__head_back + 1) % self.__max_size
        self.__tail_front = (self.__tail_front + 1) % self.__max_size
        return x


def read_input() -> List[str]:
    '''Считывает входные данные.'''

    n_commands = int(input())
    max_size_queue = int(input())
    commands = [input().split() for _ in range(n_commands)]

    return max_size_queue, commands


if __name__ == '__main__':
    max_size_queue, commands = read_input()
    queue = Deque(max_size_queue)
    for command in commands:
        try:
            if command[0] == 'push_front':
                queue.push_front(int(command[1]))
            if command[0] == 'push_back':
                queue.push_back(int(command[1]))
            if command[0] == 'pop_front':
                print(queue.pop_front())
            if command[0] == 'pop_back':
                print(queue.pop_back())

        except (DequeOverFlowError, RuntimeError) as error:
            print(error)
