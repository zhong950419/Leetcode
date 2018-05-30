# 这题目难度很高，是说一个NxN矩阵有深度，然后下雨了必须填满才能游过去，每个时间帧可以游无限的距离
#所以就变成了 m时间 0，0 到 n，n有一条连接的通路 m最小是多少
# 因为这道题说了每一个element都是unique的，所以可以通过二分来进一步缩短时间
# 主要套路还是BFS， 直接

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid)
        ans = width * width
        left = 0
        right = ans - 1
        # 这里是binary search 如果bfs成功了就找更小的可能，如果没有成功就找更大的可能
        while left <= right:
            mid = (left + right) / 2
            if self.bfs(grid, mid): 
                right = mid - 1
            else: 
                left = mid + 1
        return left
    
    def bfs(self, grid, limit):
        if grid[0][0] > limit: # limit是限制的深度 如果可以通过则证明有路径，如果不能通过则没有
            return False
        width = len(grid)
        q = [(0,0)]
        visit = set(q)
        while(q):
            x, y = q.pop(0) # bfs标准套路，用一个queue来储存可能的选择
            for dx, dy in zip((1,0,-1,0),(0,1,0,-1)): #判断可能的4个方向
                current_x = dx + x 
                current_y = dy + y 
                if (current_x < 0 or current_x >= width or current_y < 0 or current_y >= width or \
                   (current_x, current_y) in visit or grid[current_x][current_y] > limit):    
                    continue
                visit.add((current_x, current_y)) #判断所有可到达的路径 把所有的可能性入列
                q.append((current_x,current_y))
                
        return (width-1,width-1) in visit #待所有的可能性被选择之后，看是不是能到达右下角
        