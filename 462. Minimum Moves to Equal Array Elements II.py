# 这道题是问一个array要加减- 最少多少次 才能变成一个所有元素相同的array
# 那么一般这种移动的问题，都要想到中间的那个澍变化的次数最少
# 比如他给的例子 1 2 3 肯定是 1+1 3-1 移动两次 
#那么套路就比较容易了 先sort list 然后 找到中间那个
#算中间数和每一个数的差的和即可
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums is None:
            return 0
        mid = nums[len(nums)/2]
        res = 0
        for n in nums:
            res += abs(n - mid)
        return res