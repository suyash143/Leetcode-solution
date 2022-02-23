nums = [0, 1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
l = 0
for r in range(len(nums)):
    if nums[r] != 0:
        nums[r], nums[l] = nums[l], nums[r]
        l += 1
    print(nums)
print(nums)
