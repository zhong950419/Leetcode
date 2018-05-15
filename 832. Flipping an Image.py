# 这道题是说要反转一个图片
# 做法说的很清楚 一个list[list[int]]先reverselist 再将1，0交换于是按照步骤德
def flipAndInvertImage(self, A):
    for li in A:
        li.reverse()
        for ind, val in enumerate(li):
            if val == 1:
                li[ind] = 0
            else:
                li[ind] = 1
    return A
#居然还真的过了，因为是新题，还没有时间统计，估计很慢
# 想想有没有什么更好的解法，那么试试双指针
def flipAndInvertImage(self, A):
    for li in A:
        idx = 0
        lens = len(li) - 1
        while(idx <= lens-idx):
            temp = li[idx]
            
            if (li[lens-idx] == 1):
                li[idx] = 0
            else:
                li[idx] = 1
            
            if (temp == 1):
                li[lens-idx] = 0
            else:
                li[lens-idx] = 1
            
            idx = idx+1
    return A
#其实py内部的reverse应该也是这么实现的，所以说用脚本语言刷题还是感觉有种作弊的感觉23333
#第一种做法大概82ms第二种大概62ms