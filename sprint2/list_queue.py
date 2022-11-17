from typing import List


class Node:
    '''Односвязный связной список.'''

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class ListQueue:
    '''Очередь, написанная с использованием связного списка.'''

    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.size_queue = 0

    def is_empty(self):
        '''Определяет, пуста ли очередь'''

        return self.size_queue == 0

    def get(self):
        '''Выводит элемент, находящийся в голове очереди, и удаляет его.'''

        if self.is_empty():
            return print('error')

        if self.size_queue == 1:
            print(self.head.value)
            self.head = Node()
            self.tail = Node()
            self.size_queue -= 1
            return self.head.value

        if self.size_queue == 2:
            print(self.head.value)
            self.head = self.tail
            self.size_queue -= 1
            return self.head.value

        print(self.head.value)
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.size_queue -= 1

    def put(self, x):
        '''Добавляет число x в очередь.'''

        if self.is_empty():
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size_queue += 1

    def size(self):
        '''Выводит текущий размер очереди.'''

        print(self.size_queue)


def read_input() -> List[str]:
    '''Считывает входные данные.'''

    number_of_commands = int(input())
    commands = [list(map(str, input().split()))
                for i in range(number_of_commands)]
    return number_of_commands, commands


if __name__ == '__main__':
    number_of_commands, commands = read_input()
    queue = ListQueue()
    for command in commands:
        if command[0] == 'put':
            queue.put(int(command[1]))
        if command[0] == 'get':
            queue.get()
        if command[0] == 'size':
            queue.size()
