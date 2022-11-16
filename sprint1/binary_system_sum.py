from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения
    result = bin(int(first_number, 2) + int(second_number, 2))
    return result[2:]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))