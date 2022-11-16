from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    count_weather = 0
    last_idx = len(temperatures) - 1
    if len(temperatures) == 1:
        return 1
    for i in range(len(temperatures)):
        if i == 0:
            if temperatures[i] > temperatures[i + 1]:
                count_weather += 1
                continue
        if i != last_idx:
            if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
                count_weather += 1
        else:
            if temperatures[i - 1] < temperatures[i]:
                count_weather += 1
    return count_weather


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
