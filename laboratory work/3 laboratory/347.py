from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
    pairs = list(count.items())
    pairs.sort(key=lambda y: y[1], reverse=True)
    result = []
    for i in range(k):
        result.append(pairs[i][0])
    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))