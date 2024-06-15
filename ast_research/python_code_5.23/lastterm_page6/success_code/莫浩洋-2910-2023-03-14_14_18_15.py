'''一球从 h 米高度自由落下， 每次落地后反跳回原高度的 0.5倍； 再落下， 求它在第 N 次落地时， 共经过多少米？  
【输入形式】第一行输入高度，第二行输入N

【输出形式】输出两位数的浮点数'''
h= eval(input())
N= eval(input())
a=0
if N==0:
    print("0")

else:
    for i in range(N):
        if i==0:
            a+=h
        else:
            h=h*0.5
            a+=2*h
    print(a)

