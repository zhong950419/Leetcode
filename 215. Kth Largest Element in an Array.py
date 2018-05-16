#这道题需要找到array里面第k大的数值，那么套路很简单先sort在返回倒数第k个值即可

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
        