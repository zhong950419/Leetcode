#561. Array Partition I
#这道题比较trick 题目是说 给你一个2n长度的array 然后把他们分成n对，最后求出 min(pair)之和最大的解
#仔细想了一下，也就是说最好的办法就是先sort 然后两两配对，因为离的越近损失越小，那么于是就
def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return 0
    nums.sort()
    res = 0
    for idx, val in enumerate(nums):
        if (idx % 2 == 0 or idx == 0):
            res = val + res
            
    return res

# python 这个带index的for loop 实在是太蛋疼了
# nums.sort()居然return null
# 还没有+=
# 鱼唇的pypy