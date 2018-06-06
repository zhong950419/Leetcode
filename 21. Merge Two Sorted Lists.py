# 套路就是双指针直接扫一遍
# 要注意最后有可能还有list是有item的 所以要加额外判断

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        ans = ListNode(0)
        head = ans
        while(l1 and l2):
            if (l1.val < l2.val):
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        if l1 is not None:
            ans.next = l1
        if l2 is not None:
            ans.next = l2
        return head.next