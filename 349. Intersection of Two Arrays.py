#找到两个list的交集，这道题可以直接取巧把 nums1 2 中的值都放到一个set里面，然后直接最后导出set即可
# python的dict来模拟set真的好蛋疼。。。。

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if (len(nums1) == 0 or len(nums2) == 0):
            return []
        sets = {}
        ans = []
        for n in nums1:
            if (n not in sets):
                sets[n] = 1
        for m in nums2:
            if (m in sets):
                ans.append(m)
                del sets[m]
        return ans