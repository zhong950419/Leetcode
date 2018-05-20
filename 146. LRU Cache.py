#LRU 缓存 last recent use
# 这是一种缓存策略
#一般来说缓存的内存大小是有限制的，那么所谓last recent use就是当触及上限的时候 、
# 删除最不经常使用的数据
# 题目说是both O1 我的这个做法是愚蠢的做法 
# get 用O1 put要用 On
# 套路就是创造一个map来储存数据以及一个counter来表示是否常用

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.map = {}
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.map):
            self.count += 1
            self.map[key]["count"] = self.count
            return self.map[key]["value"]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if (key in self.map):
            self.count += 1
            self.map[key]["count"] = self.count
            self.map[key]["value"] = value
            return 
        
        
        
        
        if (len(self.map) >= self.capacity):
            min_key = 0
            max_counter = 99999
            for k, v in self.map.iteritems():
                if v["count"] < max_counter:   
                    if (key == 4):
                        print v["count"]
                    max_counter = v["count"]
                    min_key = k
            del self.map[min_key]
        self.count += 1
        val = {}
        val["count"] = self.count
        val["value"] = value
        self.map[key] = val

# 这是经典题，之后还是要再写一遍O1的解法 即linkedlist + hashmap的做法