import bisect
from creatRandom import *
from typing import *
import copy
from timing import timing

sample = [i for i in range(10000)]
target = 8887


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

    pos = insert(left=0, right=len(li)-1)
    li.insert(pos, t)
    return li


def recursive_binary_insert(li: List[int], t: int) -> List[int]:
    def insert(left, right):
        if left == right:
            if li[left] > t:
                return left
            else:
                return left + 1
        mid = (left+right) // 2
        if li[mid] >= t:
            return insert(left, mid)
        else:
            return insert(mid+1, right)

    pos = insert(left=0, right=len(li)-1)
    li.insert(pos, t)
    return li


def bis_binary_insert(li: List[int], t: int) -> List[int]:
    # Python build-in binary search library
    bisect.insort_left(li, t)
    return li


if __name__ == "__main__":

    @timing
    def test_correct(times):
        for i in range(times):
            li, t = random_lt_for_insert(10, (1, 100))
            li2 = copy.deepcopy(li)
            iter_binary_insert(li, t)
            bis_binary_insert(li2, t),
            print(t, li, li2, li == li2)


    @timing
    def test_iter_time(times):
        for i in range(times):
            li, t = random_lt_for_insert(10, (1, 100))
            iter_binary_insert(li, t)


    @timing
    def test_recursive_time(times):
        for i in range(times):
            li, t = random_lt_for_insert(10, (1, 100))
            recursive_binary_insert(li, t)


    @timing
    def test_bisect_time(times):
        for i in range(times):
            li, t = random_lt_for_insert(10, (1, 100))
            bis_binary_insert(li, t)


    test_iter_time(100)
    test_recursive_time(100)
    test_bisect_time(100)
    # print(timeit(stmt='bis_binary_insert(sample, target)', number=10000, globals=globals()))
    # print(timeit(stmt='recursive_binary_insert(sample, target)', number=10000, globals=globals()))
    # print(timeit(stmt='iter_binary_insert(sample, target)', number=10000, globals=globals()))
    # print(timeit(stmt="sample.index(8888)", number=10000, globals=globals()))
