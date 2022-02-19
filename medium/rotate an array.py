nums = [1,2,3,4,5,6,7,8]
k=3
n=len(nums)
k%=n
print(nums[-k:])
nums[:]=nums[-k:]+nums[:-k]
print(nums)