# 【问题描述】一球从 h 米高度自由落下， 每次落地后反跳回原高度的 0.5倍； 再落下， 求它在第 N 次落地时， 共经过多少米？  
# 【输入形式】第一行输入高度，第二行输入N

# 【输出形式】输出两位数的浮点数
# 【样例输入】

# 10

# 6
# 【样例输出】

# 29.38

h=int(input())
N=int(input())
total=-h
for i in range(N):
    total=total+h*2
    h=h*0.5
print("%.2f"%total)
