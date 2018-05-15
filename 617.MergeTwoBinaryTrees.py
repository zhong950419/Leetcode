#617. Merge Two Binary Trees
#这道题的大意大概是合并两个二叉树，如果对应的节点都有的话就求和，如果有一方没有节点的话就当0计算
#于是最先想到的就是直接递归一波直接遍历整个树
#那么先做null check，题目规则是没有节点就忽略，那么如果t1 t2中当前节点有任意一个是空，我们只需要接上剩下的树
#于是就变成
def mergeTrees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
        
#然后接下来来考虑如果t1 t2都存在的情况
#如果都存在的话，那么新树（假设叫t）的当前节点的值应该就是等于 t1 t2 这两个node的值之和
#于是变成
def mergeTrees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t = TreeNode(0)
    t.val = t1.val + t2.val

#最后来把递归的情况补上，很明显t左边的节点应该是和t1 t2 左边的节点的值有关， 右边同理
#于是变成
 
def mergeTrees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t = TreeNode(0)
    t.val = t1.val + t2.val
    t.left = self.mergeTrees(t1.left, t2.left)
    t.right = self.mergeTrees(t1.right, t2.right)
    
    return t
# 然后再回顾一下，如果t1 或t2是最后一个节点的话，下一次递归之前已经做好的null check
# 那么应该没问题了【修正了一堆语法错误】
# 于是ac了233333

