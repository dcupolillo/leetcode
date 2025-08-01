#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for n_char in range(len(haystack)):
            if haystack[n_char:n_char + len(needle)] == needle:
                return n_char

        return -1

# @lc code=end

# 83/83 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 81.86 % of python3 submissions (18 MB)

