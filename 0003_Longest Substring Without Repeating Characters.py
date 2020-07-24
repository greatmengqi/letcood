class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        start = end = 0
        max_len = 0
        index_map = {}
        while end < len(s):
            if s[end] in s[start:end]:
                start = index_map[s[end]] + 1
            else:
                index_map[s[end]] = end
                end = end + 1
                max_len = max(max_len, end - start)

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("sssass"))
