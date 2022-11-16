# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def solution(head):
    """Разворачивает двусвязный список.
    Получает голову списка. В цикле меняем ссылки с предыдущего на следующий,
    со следующего на предыдущий. Присваиваем значение головы в переменную.
    Т.к. поменяли ссылки на следующий объект головы, идем к "предыдушему" следующему.
    Когда следующего не будет, головой нового списка будет текущее значение current_head.
    """

    while head:
        head.prev, head.next = head.next, head.prev

        current_head = head  # Записываем текущее значение головы списка
        head = head.prev

    new_head = current_head
    return new_head


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()
