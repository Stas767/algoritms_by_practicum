def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return 0
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
