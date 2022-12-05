# id посылки 78763630

from typing import List


def broken_search(nums: List[int], target: int) -> int:
    start_idx = 0
    end_idx = len(nums) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if nums[mid_idx] == target:
            return mid_idx
        #  Судя по контесту, возврат из 3 известных индексов работает быстрее.
        if nums[start_idx] == target:
            return start_idx
        if nums[end_idx] == target:
            return end_idx


        elif nums[start_idx] <= nums[mid_idx]:
            if nums[start_idx] <= target <= nums[mid_idx]:
                end_idx = mid_idx - 1
            else:
                start_idx = mid_idx + 1

        else:
            if nums[mid_idx] <= target <= nums[end_idx]:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 101) == 3
