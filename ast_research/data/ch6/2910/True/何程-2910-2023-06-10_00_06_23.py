h=eval(input())
N=eval(input())
eva=h
jishu=2
while N>1:
    eva=eva+(2*h)/jishu
    jishu=jishu*2
    N-=1
print("%.2f"%eva)
