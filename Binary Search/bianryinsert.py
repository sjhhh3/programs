import bisect
from creatRandom import *
from typing import *
import copy

sample = [1, 3, 5, 7, 9]
target = 0


def iter_binary_insert(li: List[int], t: int) -> List[int]:
    # Providing the function of searching and inserting the target when t in or not in li
    def insert(left, right):
        while left <= right:
            if left == right:
                if li[left] > t:
                    return left
                else:
                    return left + 1
            else:
                mid = (left+right) // 2
                if li[mid] >= t:
                    right = mid
                else:
                    left = mid + 1
        return left

    pos = insert(left=0, right=len(li) - 1)
    li.insert(pos, t)
    return li


def bis_binary_insert(li: List[int], t: int) -> List[int]:
    # Python build-in binary search library
    bisect.insort_left(li, t)
    return li


if __name__ == "__main__":

    for i in range(16):
        li, t = random_lt_for_insert(10, (1, 100))
        li2 = copy.deepcopy(li)
        iter_binary_insert(li, t)
        bis_binary_insert(li2, t),
        print(t, li, li2, li == li2)