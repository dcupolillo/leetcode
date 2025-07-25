#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
        values = [map[char] for char in s]
        for n, value in enumerate(values):
            if n == len(values) - 1:
                break
            if value < values[n + 1]:
                values[n] = values[n + 1] - value
                values.remove(values[n + 1])

        return sum(values)
                
# 3999/3999 cases passed (8 ms)
# Your runtime beats 26.41 % of python3 submissions
# Your memory usage beats 20.59 % of python3 submissions (18 MB)
                
