class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            boo = guess(mid)
            if boo == 0:
                return mid
            elif boo == 1:
                low = mid + 1
            else:
                high = mid - 1
