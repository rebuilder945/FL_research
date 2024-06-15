#一球从 h 米高度自由落下,每次落地后反跳回原高度的 0.5倍;再落下
# 求它在第 N 次落地时， 共经过多少米？  
h = eval(input())
N = eval(input())
s = h
for i in range(N):
    h = 0.5 * h
    s = s + 2*h
print(".2f"%s) 

