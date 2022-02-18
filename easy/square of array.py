sorted = []
nums = [-4, -1, 0, 3, 10]
left = 0
right = len(nums) - 1
print(right)
while left <= right:
    lf = nums[left] * nums[left]
    rt = nums[right] * nums[right]
    print(left, right)
    print(lf, rt)

    if lf > rt:
        sorted.append(lf)
        left += 1
    else:
        right -= 1
        sorted.append(rt)
    print(nums, sorted)
    print()

print(nums, sorted)
