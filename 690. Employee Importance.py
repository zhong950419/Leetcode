# 一道搜索类的题，因为tag是bfs 先想了想感觉挺麻烦的，
# 于是切一波dfs，果断容易多了
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def dfs(maps, e):
            i = e.importance
            for s in e.subordinates:
                i += dfs(maps, maps[s]) #这里return每一个employee的价值 所以直接加上dfs即可

            return i
        maps = {} 
        for e in employees:
            maps[e.id] = e# 起手先把所有的employee放到map里面，这样后面访问会比较容易，因为只有id 
        print maps[id].importance
        
        return dfs(maps, maps[id])    
 