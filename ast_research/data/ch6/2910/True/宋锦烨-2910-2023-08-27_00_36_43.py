#一球从 h 米高度自由落下， 每次落地后反跳回原高度的 0.5倍； 再落下， 求它在第 N 次落地时， 共经过多少米？  

#第一行输入高度，第二行输入N

#输出两位数的浮点数
h=eval(input())
N=eval(input())
l=0      #累计的l
for i in range(0,N-1):
    L=h+h/2#这一次的l
    l=l+L
    h=h/2
l=l+h
print('%.2f'%l)


    
    
