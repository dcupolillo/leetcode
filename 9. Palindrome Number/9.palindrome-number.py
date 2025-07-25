#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.

        Return
        -------
        bool: True if x is a palindrome, False otherwise.
        """

        # # Constraints
        # if -2**31 <= x <= 2**31 - 1:
        #     raise ValueError("x should be between -2^31 and 2^31 - 1.")

        if str(x) == str(x)[::-1]:
            return True
        
        return False
        
# @lc code=end

# 11511/11511 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 88.95 % of python3 submissions (17.7 MB)