from typing import List, Tuple, Optional
import time


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    '''Оптимизация алгоритма добавлением оперативной памяти.'''

    additional_memory = set()

    for second_value in arr:
        first_value = target_sum - second_value
        if first_value in additional_memory:

            return first_value, second_value

        additional_memory.add(second_value)
    
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())

    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

start_time = time.time()
arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
print(time.time() - start_time)
