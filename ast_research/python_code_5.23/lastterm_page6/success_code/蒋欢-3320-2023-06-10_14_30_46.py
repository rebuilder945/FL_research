def juxing(a,b):
    if a<0 or b<0:
        print('illegal data')
    elif a==b:
        print("It's a square")
    else:
        print("It's a rectangle")
a=eval(input())
b=eval(input())
juxing(a,b)
