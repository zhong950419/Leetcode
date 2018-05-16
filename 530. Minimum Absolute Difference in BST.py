#题目是求一个bst里面最小差距的两个节点
#那么一看这里是个bst 很明显数据是有序排列的，那么差距最小的肯定是其中两个连在一起的
#那么很明显使用中序遍历就可以把bst当作sortedarray来看
#然后我们只需要求解出上一个node和当前node的差即可
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = 100000
        self.minum = 100000
        def recursor(root):
            if (root.left is not None):
                recursor(root.left)
            self.minum = min(self.minum,abs(root.val-self.prev))
            self.prev = root.val
            #主要还是在这里，居然不能直接用外面的minum和prev简直是太愚蠢了
            #minum用来储存结果prev用来储存上一个节点。。
            #这样的话就是从左下开始顺序遍历
            #其实最好理解的方式还是转成sortedarray然后在loop一遍
            #总之复杂度都是On 233

            if (root.right is not None):
                recursor(root.right)
                
        
        if root is None:
            return 0
        recursor(root)
        
        return self.minum

