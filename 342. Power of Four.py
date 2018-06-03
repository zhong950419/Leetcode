# 判断一个数字是不是4的次方数


#重点在于要做一个非0判断 不然会导致除0问题
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while((num % 4 == 0) and num != 0) :
            num /= 4
        
        
        return num == 1