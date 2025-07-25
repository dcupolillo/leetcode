#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(
            self,
            nums: list,
            val: int
    ) -> int:
        
        if len(nums) < 0 and len(nums) > 100:
            raise ValueError("Length of `nums` should be included between 0-100.")

        if val < 0 and val > 100:
            raise ValueError("`val` should be between 0-100.")

        if sum([True for num in nums if num < 0 and num > 50]) > 0:
            raise ValueError("Values in `nums` should be between 0-50.")
        
        indices = [i for i, num in enumerate(nums) if num == val]

        k = len([v for v in nums if v != val])
        for index in sorted(indices, reverse=True):
            del nums[index]

        return k
        
# @lc code=end

