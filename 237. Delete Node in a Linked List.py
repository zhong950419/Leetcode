#删除一个lindelist当前的node
#只给出当前的node的访问
#不知道linkedlist是啥可以来wx我23333
#一般linkedlist删除都是直接xx.next = xx.next.next
#这个不给之前的node的访问的话就直接用后面的node替换就好了
#有个问题是，有可能最后一个node是tail了那么就让next=none就ok了 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        if (node.next.next is not None):
            node.next = node.next.next
        else:
            node.next = None
        