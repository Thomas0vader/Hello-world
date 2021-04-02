#tiaoguo 7 he 7 de beishus
# a = 10
#
# for x in range(1,101):
# 	if x%7 == 0 or x%10 ==7 or int(x/10) == 7:
# 		continue
# 	else:
# 		print(x)
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()


