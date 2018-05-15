#654. Maximum Binary Tree
#还是二叉树相关的，根据一个list构建一个最大的二叉树
#题目上说，当前的root应该是当前list中最大的，而root的左右的子树就是以当前值的index 为分界的两个list中构造
#所以还是第一时间想到了递归 = =

#一开始还是要做个终止判断，如果是最后一个node了那么nums肯定是空的 所以应该
def constructMaximumBinaryTree(self, nums):
    if not nums:
        return

#接下来就是怎么切这个list了 【python的list操作真是独树一帜啊
#于是就先去拿到当前的val然后切好array
def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        index = nums.index(max(nums))
        current = max(nums)
        left = nums[0:index]
        right = nums[index+1:]

#最后还是新建一棵树并递归求解
def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        index = nums.index(max(nums))
        current = max(nums)
        t = TreeNode(current)
        t.left = self.constructMaximumBinaryTree(nums[0:index])
        t.right = self.constructMaximumBinaryTree(nums[index+1:])
        return t
#不过就是速度有点慢 