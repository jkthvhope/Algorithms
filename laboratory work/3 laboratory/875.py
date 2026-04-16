import math


def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    while left < right:
        mid = (left + right) // 2
        total_time = 0
        for p in piles:
            total_time += math.ceil(p / mid)
        if total_time <= h:
            right = mid
        else:
            left = mid + 1
    return left


print(minEatingSpeed([3,6,7,11],8))