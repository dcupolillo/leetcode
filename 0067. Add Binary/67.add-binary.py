#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        base_10 = 0
        for number in [a, b]:
            for n, digit in enumerate(number[::-1]):
                base_10 += int(digit) * 2 ** n

        return bin(base_10)[2:]
# @lc code=end

# 296/296 cases passed (3 ms)
# Your runtime beats 44.18 % of python3 submissions
# Your memory usage beats 27.84 % of python3 submissions (17.9 MB)