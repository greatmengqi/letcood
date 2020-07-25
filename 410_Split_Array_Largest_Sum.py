class Solution:
    def splitArray(self, nums, m: int) -> int:

        def check(x):
            total = 0
            cnt = 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num

            return cnt <= m

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if (check(mid)):
                right = mid
            else:
                left = mid + 1

        return left
