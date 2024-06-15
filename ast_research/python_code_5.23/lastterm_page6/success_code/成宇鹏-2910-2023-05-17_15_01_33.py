# 一球从 h 米高度自由落下， 每次落地后反跳回原高度的 0.5倍； 再落下， 求它在第 N 次落地时， 共经过多少米？  

h = int(input())
N = int(input())
s1 = h
a = 1
s = 0
while a < N :
    s += 0.5*h*2
    h = 0.5*h
    a += 1
s += s1
print("%.2f"%s)
