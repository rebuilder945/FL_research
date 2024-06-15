a=eval(input())
b=eval(input())
if a!=0 and b!=0 and a==b:
    print("it's a square")
elif a!=b and a>0 and b>0:
    print("it's a rectangle")
elif a<=0 or b<=0:
    print('illegal data')
