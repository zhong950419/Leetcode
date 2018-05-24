# 这道题是说给一个nums lst 然后 每个值都要相除，找到最大的就好了
# 思考了一下 [a, b, c] 最大的一定是 a/(b/c) 因为 a / (b/c) = a /b * c
#那么就直接string搞一遍
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        ans = str(nums[0]) + "/(" + str(nums[1])
        for idx, val in enumerate(nums):
            if idx > 1:
                ans = ans + "/" + str(val)
                
        return ans + ")"
        
            
        