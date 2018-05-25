#这道题是找到不重复的char的位置
#其实很简单 扫一遍建立一个map
#然后只要保证只出现过一次就return即可
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for c in s:
            if c in letters:
                letters[c] = letters[c] + 1 
            else:
                letters[c] = 1
                
        for i in xrange(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1