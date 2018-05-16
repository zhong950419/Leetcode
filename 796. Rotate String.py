#这题的意思是说判断string A 是否可以以某种方式切一刀重组之后变成B
#这题看了答案
#一开始是想，直接loop一遍A 切i to end 然后看B中是否存在如果存在在看另外一部分是否匹配
#然后发现find要考虑各种情况，比如是开始 是结尾etc 。
#然后时间到了，去看了一下网上的做法，很简单，就是每次切开之后直接重组看是不是和B相同
#我简直是太愚蠢了 这么简单的方法都没想到



class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A is None or B is None:
            return False
        if A == "" and B == "":
            return True
        
        if len(A) != len(B):
            return False
        
        
        for index in range (len(A)):
            if (A[index:] + A[:index] == B):
                return True
        
        return False