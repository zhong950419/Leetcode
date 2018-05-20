#从二叉树构建一个string
#很容易其实就是loop一遍
#然后根据当前节点的子节点不同的情况直接加不同的str就好了

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def recursor(root):
            if root is None:
                return ""
            ans = str(root.val)

            if (root.left is not None and root.right is not None):
                return ans + "(" + recursor(root.left) + ")" + "(" + recursor(root.right) +")"
            elif root.left is not None:
                return ans + "(" + recursor(root.left) + ")"
            elif root.right is not None:
                return ans + "()" + "(" + recursor(root.right) + ")"
            else:
                return ans
        return recursor(t)