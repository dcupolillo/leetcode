#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        counter = 1
        
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[counter] = nums[n]
                counter += 1

        return counter

# 362/362 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 48.29 % of python3 submissions (19 MB)
