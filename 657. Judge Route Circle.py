#657. Judge Route Circle
#String 相关的问题，给出一个string描述机器人的移动方向 U = 上 D = 下 L = 左 R = 右，
#问移动完是否还在同一个点
# 那么一开始的思路就是从水平和垂直方向来考虑也就是说只要UD和LR共用一个变量
def judgeCircle(self, moves):
    horz = 0
    vert = 0
    for c in moves:
        if (c == "U"):
            vert = vert+1
        if (c == "D"):
            vert = vert-1
        if (c == "L"):
            horz = horz+1
        if (c == "R"):
            horz = horz-1
    if (horz == 0 and vert == 0):
        return True
    else:
        return False
# 这到底感觉还是比较简单的，也没有什么陷阱2333 除了python没有++ -- 这类运算符让人比较烦躁。

                