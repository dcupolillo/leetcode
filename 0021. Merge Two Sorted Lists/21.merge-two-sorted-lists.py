#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        merged_values = []
        for _list in [list1, list2]:

            if _list is None:
                continue
            
            first_value = _list.val
            following_values = _list.next

            values = [first_value]
        
            while following_values:
                following_value = following_values
                values.append(following_value.val)
                following_values = following_values.next

            merged_values.extend(values)
        
        sorted_values = sorted(merged_values)

        output = None

        while sorted_values:

            value = sorted_values.pop(0)

            if output is None:
                output = ListNode(value)
                current_node = output
            else:
                current_node.next = ListNode(value)
                current_node = current_node.next

        return output
    
# @lc code=end
        
# 208/208 cases passed (1 ms)
# Your runtime beats 19.04 % of python3 submissions
# Your memory usage beats 37.86 % of python3 submissions (17.8 MB)


