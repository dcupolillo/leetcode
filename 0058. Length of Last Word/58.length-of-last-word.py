#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len([word for word in s.split(" ") if word != ""][-1])
    


# @lc code=end

# 60/60 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 17.51 % of python3 submissions (18.1 MB)
