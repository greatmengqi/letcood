class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()
        len = 0
        startindex = -1
        for (index, value) in enumerate(s):
            if value in map.keys():
                if startindex < map[value]:
                    startindex = map[value]
            if index - startindex > len:
                len = index - startindex
            map[value] = index
        return len


s = Solution()
print(s.lengthOfLongestSubstring("sssss"))
