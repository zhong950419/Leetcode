# 145. Binary Tree Postorder Traversal
# 思路和之前那道一样
# 不过顺序是这样的
#                         1
#              2                    3
#     4            5       6              7
#  8
# 8 4 5 2 6 7 3 1
#简单的来说还是从左往右扫，不过就是要等到最后一个了，才能开始加 然后依然是先左后右


def postorderTraversal(self, root):
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
    if (root.right is not None):
        self.traversal(root.right, li)
    
    li.append(root.val)