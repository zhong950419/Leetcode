#这道题是要去掉一个二叉树里面多余的部分，如果都是0整棵树都砍掉。
# 那么如果递归的话，就发现如果最底层有0的node就直接砍，那么直接递归就ok
# 也就是说从最底层开始砍，只要当前node左右都为空且为0 则gg

 def pruneTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    
    if root is None:
        return root
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    
    if (root.left is None and root.right is None and root.val == 0):
        root = None
    
    return root
#值得注意的是要 先算左右树再考虑是否删除当前节点，不然又会出现尴尬的情况