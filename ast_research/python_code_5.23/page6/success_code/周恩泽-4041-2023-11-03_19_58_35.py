n1=eval(input())
n2=eval(input())
if n1<0 or n2<0 :
    print("illegal data")
elif n1>0 and n2>0 and n1==n2:
    print("It's a square")
elif n1>0 and n2>0  and n1!=n2:
    print("It's a rectangle")
else:
    print("illegal data")


