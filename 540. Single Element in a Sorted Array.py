#找出一个sorted array 里面不成对的值
# 如 【1，1，2】则返回2



#这题乍一看很简单，index 为奇数相加，偶数相减，那么最后剩下的就是多出来的那个
#那么久套路一波

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        
        length = len(nums)
        res = 0
        for idx, val in enumerate(nums):
            if (idx % 2 == 0):
                res = val + res
            else:
                res = res - val
        
        return res

# 就这么ac了
# 题目接下来又说 给定时间Ologn 那么肯定是要求用二分搜索了，那么想想 这个list的length肯定是奇数
# ，那么从中间开始如果mid和mid+1不一致就是在前半个list 一致就在后半个
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        
        r = len(nums) -1 
        l = 0
        while (l < r):
            m = (l + r)/2
            if(m%2==1):
                m-=1

        
                
            if (nums[m+1] != nums[m]):
                r=m
            else:
                l = m+2
        
        return nums[l]
            