def findMaxAverage_cw(nums, k):
    tekysh_sum = sum(nums[:k])
    max_sum = tekysh_sum

    for i in range(k, len(nums)):
        tekysh_sum += nums[i] - nums[i - k]

        if tekysh_sum > max_sum:
            max_sum = tekysh_sum

    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage_cw(nums, k))