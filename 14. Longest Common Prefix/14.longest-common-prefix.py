#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(
            self,
            strs: list
    ) -> str:

        common_prefix = ""

        shortest_string = min(strs, key=len)
        
        for n_char, char in enumerate(shortest_string):
            
            if not all(s[n_char] == char for s in strs):
                break
            
            common_prefix += char

        return common_prefix
# @lc code=end

# 126/126 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 30.61 % of python3 submissions (18 MB)