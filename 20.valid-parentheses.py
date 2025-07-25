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

        if s[0] not in match_map.keys():
            return False

# @lc code=end

