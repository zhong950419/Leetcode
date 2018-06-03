# 判断两个词是不是同构的
# 重点在于从map里面删东西的时候要额外判断一下这个char是否还在map中

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps = {}
        for c in s:
            if (c not in maps):
                maps[c] = 1
            else:
                maps[c] += 1
                
        for c in t:
            if (c not in maps):
                return False
            if (maps[c] == 1):
                del maps[c]
            else:
                maps[c] -= 1
        
        if len(maps) == 0:
            return True
        else:
            return False