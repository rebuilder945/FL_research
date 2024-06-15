def judge(a,b):
    if a<=0 or b<=0:
        return "illegal data"
    elif a==b:
        return "It's a square"
    else:
        return "It's a rectangle"
a=eval(input())
b=eval(input())
print(judge(a,b))
