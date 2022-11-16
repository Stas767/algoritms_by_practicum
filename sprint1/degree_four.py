def is_power_of_four(number: int) -> bool:
    tmp = 1
    while tmp < number:
        tmp *=4
    return tmp == number

print(is_power_of_four(int(input())))