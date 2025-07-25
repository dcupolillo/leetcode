#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(
            self,
            nums: list,
            target: int
    ) -> list:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        
        Notes
        ------
        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.
        """

        # Costraints
        if len(nums) < 2 or len(nums) > 10**4:
            raise ValueError("Length of `nums` should be between 2 and 10^4.")
       
        if target < -10**9 or target > 10**9:
            raise ValueError("`target` should be between -10^9 and 10^9.")
        
        for num in nums:
            if num < -10**9 or num > 10**9:
                raise ValueError("Values in `nums` should be between -10^9 and 10^9.")
        
        if len(nums) == 2:
            return [0, 1]
        
        for n_row, row in enumerate(nums):
            for n_col, col in enumerate(nums):
                if n_col <= n_row:
                    continue
        
                if row + col == target and n_row != n_col:
                    return [n_row, n_col]

# 63/63 cases passed (3124 ms)
# Your runtime beats 5.49 % of python3 submissions
# Your memory usage beats 99.02 % of python3 submissions (18.2 MB)

