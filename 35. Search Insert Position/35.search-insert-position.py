#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # # Linear solution
        # if target in nums:
        #     return nums.index(target)
        # 
        # else:
        #     new_nums = sorted(nums + [target])
        #     return new_nums.index(target)

        # Logarithmic runtime complexity
        left, right = 0, len(nums) - 1

        while left <= right:
            middle_point = (left + right) // 2

            if nums[middle_point] == target:
                return middle_point
            
            elif nums[middle_point] < target:
                left = middle_point + 1
            else:
                right = middle_point - 1
# 
        # return left

# Linear solution
# 66/66 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 43.43 % of python3 submissions (18.4 MB)

# Logartihmic solution
# 66/66 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 25.76 % of python3 submissions (18.5 MB)
        
# @lc code=end

