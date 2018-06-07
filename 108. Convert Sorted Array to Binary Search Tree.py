#这道题还是老套路，所谓bst本身就是用binary search的方式表示一个有序的容器而已
# 所以直接用binary search递归就好了
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        return self.recursor(nums, 0 , len(nums)-1)
        
    
    def recursor(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right-left) /2
        node = TreeNode(nums[mid])
        node.left = self.recursor(nums, left, mid-1)
        node.right = self.recursor(nums, mid+1 ,right)
        return node        