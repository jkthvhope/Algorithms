# 69

def my_sqrt(x):
    if x < 2:
        return x
    left = 0
    right = x
    while left <= right:
        mid = (right + left) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(my_sqrt(4))