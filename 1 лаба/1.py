nums = [3, 2, 4]
target = 6

nums_2 = []
for i in range(len(nums)):
    nums_2.append([nums[i], i])
nums_2.sort()

left = 0
right = len(nums) - 1
itog = []

while left < right:
    two_sum = nums_2[left][0] + nums_2[right][0]
    if two_sum == target:
        itog = [nums_2[left][1], nums_2[right][1]]
        break
    elif two_sum < target:
        left += 1
    else:
        right -= 1
print(itog)