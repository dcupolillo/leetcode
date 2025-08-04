#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        _sum = 0
        for n, digit in enumerate(digits[::-1]):
            _sum += digit * 10 ** n

        _sum += 1

        return [int(i) for i in list(str(_sum))]
# @lc code=end  

# 111/111 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 49.01 % of python3 submissions (17.7 MB)