class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)

        if (m > n):
            return self.findMedianSortedArrays(nums2, nums1)

        l1 = r1 = l2 = r2 = None

        c1 = c2 = 0

        lo = 0  # lo为偶数
        hi = 2 * m  # 添加m+1个空格，故最大值得下标是2m,h1为偶数

        while lo <= hi:
            c1 = (lo + hi) // 2
            c2 = m + n - c1

            l1 = -100000 if c1 == 0 else nums1[(c1 - 1) // 2]
            r1 = 100000 if c1 == 2 * m else nums1[c1 // 2]
            l2 = -100000 if c2 == 0 else nums2[(c2 - 1) // 2]
            r2 = 100000 if c2 == 2 * n else nums2[c2 // 2]

            if (l1 > r2):
                hi = c1 - 1
            elif (l2 > r1):
                lo = c1 + 1
            else:
                break
            print((max(l1, l2) + min(r1, r2)) / 2)
        return (max(l1, l2) + min(r1, r2)) / 2


s = Solution()
s.findMedianSortedArrays([1, 2], [3, 4])
