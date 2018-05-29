#判断一个数字是不是可以self divde 也就是类似于123 这种要对 1 2 3 分别取模
# 一开始没仔细看题，栽倒了0上面
# 然后其实很简单就是遍历一遍然后每一个求值即可

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            if "0" in str(i):
                continue
            else:
                temp = 0
                for c in str(i):
                    temp += i % int(c)
                if temp == 0:
                    res.append(i)
                        
        return res
            