#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:

        match_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        open_brackets = []
        for char in s:
            if char in match_map:
                open_brackets.append(char)
            else:
                if not open_brackets or char != match_map[open_brackets[-1]]:
                    return False
                open_brackets.pop()

        return not open_brackets

# @lc code=end

# 100/100 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 50.75 % of python3 submissions (17.8 MB)

            
