#删掉一个linkedlist里面同样的数量
#这个其实之前用js做过一次，用了取巧的方法先转linkedlist to array然后正常遍历array
#今天用正常的做法，想了半天还是只会用快慢指针
#先新建一个变量来做头，然后要存下这个位置，不然最后没得return
#linkedlist最烦的就是这个
# 然后就变成 pre -> heda -> other linkedlist
#             p1   p2
# 那么我们还是从head 也就是p2往下走，遇到了val相同的 直接把p1.next 变成p2.next
# 然后其他时候p1 正常走
# p2则需要每次都向下走
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ListNode(-9999999)
        ans = pre
        pre.next = head
        while(head is not None):
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return ans.next