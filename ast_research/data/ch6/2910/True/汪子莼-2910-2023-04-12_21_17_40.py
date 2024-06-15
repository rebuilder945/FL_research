height=eval(input())
N=eval(input())
l=0
while N>1:
    l+=height*3/2
    height=height/2
    N-=1
l+=height
print("%.2f"%l)
