#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(
            self,
            nums1: list,
            m: int,
            nums2: list,
            n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        assert len(nums1) == m + n, f"nums1 should have a lenght of {m + n}"
        assert len(nums2) == n, f"nums2 should have a lenght of n = {n}"
        
        if m < 0:
            raise ValueError("m should be >= 0.")
        
        if n > 200:
            raise ValueError ("n should be <= 200.")
        
        if (m + n) < 1 and (m + n) > 200:
            raise ValueError("m + n should be included between 1 and 200.")

        if m == 0:
            del nums1[:]
        if n!= 0:
            del nums1[m:]
        
        nums1.extend(nums2[:n])
        nums1.sort()

# @lc code=end

# 59/59 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 25.43 % of python3 submissions (29.3 MB)