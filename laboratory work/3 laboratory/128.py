from typing import List


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    max_length = 0
    for i in num_set:
        if (i - 1) not in num_set:
            first_num = i
            length = 1
            while (first_num + 1) in num_set:
                first_num += 1
                length += 1
            if length > max_length:
                max_length = length
    return max_length

print(longestConsecutive([100, 4, 200, 1, 3, 2]))