class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict()
        for i in range(len(nums)):
            m[nums[i]] = [i, target - nums[i]]

        for i in range(len(nums)):
            if m[nums[i]][1] in m and  m[m[nums[i]][1]][1] == nums[i] and m[m[nums[i]][1]][0] != i:
                if m[m[nums[i]][1]][0] < i:
                    print((m[m[nums[i]][1]][0], i))
                    return list((m[m[nums[i]][1]][0], i))
                else:
                    print((i, m[m[nums[i]][1]][0]))
                    return list((i, m[m[nums[i]][1]][0]))


s = Solution()
s.twoSum([2, 5, 5, 15], 10)
