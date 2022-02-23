numbers = [2, 7, 11, 15]
target = 9


# solution 1 but slow speed
def bin_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


for i in range(len(numbers)):
    initial = numbers[i]
    low = i
    high = len(numbers) - 1
    find = target - initial
    res = bin_search(numbers, low + 1, high, find)
    if res != -1:
        print([i + 1, res + 1])
    else:
        pass

# solution 2

left = 0
right = len(numbers) - 1

while left < right:
    checksum = numbers[left] + numbers[right]

    if checksum == target:
        # return [left + 1, right + 1]
        pass

    if checksum > target:
        right -= 1

    else:
        left += 1

# return -1
