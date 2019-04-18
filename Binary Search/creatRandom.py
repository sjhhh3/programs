import random
from typing import *


def random_lt_for_search(length: int, ranging: Tuple[int, int]) -> Tuple[List[int], int]:
    start, end = ranging
    randomlist = [random.randint(start, end) for _ in range(length)]
    randomlist.sort()
    tar = randomlist[random.randint(0, len(randomlist)-1)]
    return randomlist, tar


def random_lt_for_insert(length: int, ranging: Tuple[int, int]) -> Tuple[List[int], int]:
    start, end = ranging
    randomlist = [random.randint(start, end) for _ in range(length)]
    randomlist.sort()
    tar = random.randint(start-20, end+20)
    return randomlist, tar