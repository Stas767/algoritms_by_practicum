from typing import List


def merge(arr: List[int], lf: int, mid: int, rg: int) -> List[int]:
    # Your code
    # “ヽ(´▽｀)ノ”
    left = arr[lf:mid]
    right =arr[mid:rg]
    l = r = 0
    k = lf
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        arr[k] = right[r]
        r += 1
        k += 1

    return arr


def merge_sort(arr: List[int], lf: int, rg: int) -> None:
    # Your code
    # “ヽ(´▽｀)ノ”
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected