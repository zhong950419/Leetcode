#94. Binary Tree Inorder Traversal
#这让道题大概是说把binary tree 扫一遍，按特定顺序加入一个list
#inorder的顺序是从左到右，于是还是老样子recursive，不过这次需要一个变量来储存list
def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    li = []
    self.traversal(root, li)
    return li
        
def traversal(self, root, li):
    if (root.left is not None):
        self.traversal(root.left, li)
    li.append(root.val)
    if (root.right is not None):
        self.traversal(root.right, li)
#一开始被这个order搞的有些糊涂，其实一颗类似如下的树
#                         1
#                 2                3
#          4          5       6          7
#     8
#结果应该是 8 4 2 5 1 6 3 7
# 就是说从左下开始 左中右，这么扫过去，视觉上看应该是斜着过去的

#不过有个锅是没考虑到一开始root为空的情况 加上
def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if (root is None):
        return []
    li = []
    self.traversal(root, li)
    return li
    
def traversal(self, root, li):
    if (root.left is not None):
        self.traversal(root.left, li)
    li.append(root.val)
    if (root.right is not None):
        self.traversal(root.right, li)
# 然后ac
