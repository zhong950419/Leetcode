#669. Trim a Binary Search Tree
#这道题大概是说 清理一个bst 使得其中所有的值小于规定的LR
#这道题想了蛮久，还看了答案才写出来
#一开始思路是这样的，bst的left<root right>root 那么又要用递归遍历一遍
#如果当前节点比L小的话，那么当前节点左边的树可以全部gg，同理右边也是如此
#这是因为bst的性质
#copy自wiki
#若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
#若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
#任意节点的左、右子树也分别为二叉查找树；
#没有键值相等的节点。
def trimBST(self, root, L, R):
    if root == None:
        return None            
    
    if root.val < L:
        return self.trimBST(root.right, L, R)
    if root.val > R:
        return self.trimBST(root.left, L, R)
    
    self.trimBST(root.left, L, R)
    self.trimBST(root.right, L, R)
    return root
#然而怎么都是不过，想了半天也没想出个所以然来
#正确答案是这样的
def trimBST(self, root, L, R):
    if root == None:
        return None            
    
    if root.val < L:
        return self.trimBST(root.right, L, R)
    if root.val > R:
        return self.trimBST(root.left, L, R)
    
    root.left = self.trimBST(root.left, L, R)
    root.right = self.trimBST(root.right, L, R)
    return root
#这次主要问题在于最后没有写root.left和root.right那么就没有重置左右树gg
#鱼唇
