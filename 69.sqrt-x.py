#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        # n = 1
        # while n * n <= x:
        #     n += 1
        #     
        # return n - 1
    
        # 1019/1019 cases passed (992 ms)
        # Your runtime beats 13.98 % of python3 submissions
        # Your memory usage beats 96.33 % of python3 submissions (17.5 MB)

        # This solution uses linear search, which is inefficient for large x.
        # A more efficient solution would be to use binary search or Newton's method.

        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
        # 1019/1019 cases passed (0 ms)
        # Your runtime beats 100 % of python3 submissions
        # Your memory usage beats 81.38 % of python3 submissions (17.7 MB)

    
        

# @lc code=end

