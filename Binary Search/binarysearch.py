import bisect
from creatRandom import *
from typing import *

# sample = [1, 3, 5, 7, 9]
# target = 9


def iter_binary_search(li: List[int], t: int) -> int:
    # Only provide the function of searching the index when t in li

    left = 0
    right = len(li) - 1
    while left < right:
        mid = (left+right) // 2
        # if li[mid] == t:
        #     return mid
        if li[mid] >= t:   # If remove =, we have to add if li[mid] == t above, if add, means let left approach
            right = mid
        else:
            left = mid + 1
    return left


def recursive_binary_search(li: List[int], t: int) -> int:
    def recur(left: int, right: int) -> int:
        if left < right:
            mid = (left+right) // 2
            # if li[mid] == t:
            #     return mid
            if li[mid] >= t:
                return recur(left, mid)
            else:
                return recur(mid+1, right)
        else:
            return left
    return recur(0, len(li)-1)


def bis_binary_search(li: List[int], t: int) -> int:
    # Python build-in binary search library
    return bisect.bisect_left(li, t)


if __name__ == "__main__":

    for i in range(16):
        li, t = random_lt_for_search(10, (1, 100))
        print(li, t, iter_binary_search(li, t), bis_binary_search(li, t), \
              recursive_binary_search(li, t),\
              iter_binary_search(li, t) == bis_binary_search(li, t) == recursive_binary_search(li, t))
