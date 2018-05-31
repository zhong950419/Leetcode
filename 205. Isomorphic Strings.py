# 判断string是否是isomorphic 诸如aab bbc 这种格式类似
#套路就是把这两个string转换成数字好了 比如aab类似可以转换成112
#其中用个map来储存char所对应的数字

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        i_s = ""
        i_t = ""
        map_s = {}
        map_t = {}
        for c in s:
            if (c not in map_s):
                map_s[c] = i
                i_s += str(i)
                i += 1
            else:
                i_s += str(map_s[c])
        for c in t:
            if (c not in map_t):
                map_t[c] = j
                i_t += str(j)
                j += 1
            else:
                i_t += str(map_t[c])
                
            
        return i_s == i_t