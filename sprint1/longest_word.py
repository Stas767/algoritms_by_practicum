def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    longest_word = 0
    for word in range(1, len(line)):
        if len(line[word]) > len(line[longest_word]):
            longest_word = word
    return line[longest_word]

def read_input() -> str:
    _ = input()
    line = input().strip().split()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
