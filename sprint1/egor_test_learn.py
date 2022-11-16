from textwrap import dedent
from io import StringIO
from sys import stdin  # 1. импортировали


def _input(_in=stdin):  # 2. добавили
    l = "not_end"
    k = []
    while True:
        l = _in.readline()  # 3. input() => readline()
        if l != "end":
            k.append([int(i) for i in l.split()])
        else:
            break


# 1. test ok
assert _input(StringIO("""1
end""")) == [[1]]

# 2. test ok
_test_input_2 = dedent("""
    9 5 3
    0 7 -1
    -5 2 9
    end
""").strip()

answer2 = [
    [9, 5, 3],
    [0, 7, -1],
    [-5, 2, 9],
]

assert _input(StringIO(_test_input_2)) == answer2

# 3. test fail
assert _input(StringIO("1\nend")) == [[3]]
