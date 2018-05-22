# inmemory的合并两个排序后的list
# 之前废了好大力气都没做出来
#今天换了个思路，倒着来双指针一波，就差不多了
#答案在这里
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 
        p = m -1
        q = n -1
        while (p >= 0) and (q >= 0):
            if nums1[p] > nums2[q]:
                nums1[p+q+1] = nums1[p]
                p -= 1
            else:
                nums1[p+q+1] = nums2[q]
                q -= 1
        nums1[:q+1] = nums2[:q+1]
# 套路就是倒着扫然后算成型的index/offset
