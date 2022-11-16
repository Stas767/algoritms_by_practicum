from typing import List


def factorize(number: int) -> List[int]:
    simple_list = []
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            simple_list.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        simple_list.append(number)
    return simple_list

result = factorize(int(input()))
print(" ".join(map(str, result)))
