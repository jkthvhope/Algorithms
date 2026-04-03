height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height) - 1
square = 0
while left < right:
    width = right - left

    if height[left] < height[right]:
        h = height[left]
    else:
        h = height[right]

    square_peremen = width * h

    if square_peremen > square:
        square = square_peremen

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(square)