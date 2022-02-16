pos2 = 0
nums = [3, 3]

target = 6
count = 0
for i in nums:
    print(i, count)
    print(nums[count + 1:])
    if (target - i) in nums[count + 1:]:
        new = nums[count + 1:]

        pos2 = nums.index((target - i), count + 1)
        print(f"[{nums.index(i)},{pos2}]")
        break
    else:
        print(count)
        count += 1
