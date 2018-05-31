# 这道题比较简单 J 代表了珠宝的属性 S代表矿石，问s中有多少宝石
# 直接loop一遍J然后求s.count求和即可
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for j in J:
            num = S.count(j)
            ans += num
        return ans
            