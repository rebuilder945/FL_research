chang=eval(input())
kuan=eval(input())
if kuan or chang<=0:
    print("illegal data")
elif kuan==chang:
    print("It's a square")
elif kuan!=chang:
    print("It's a rectangle")
