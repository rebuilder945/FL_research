l = eval(input())
w = eval(input())
if l<=0 or w<=0:
    print("illegal data")  
elif l != w:
    print("It's a rectangle")
elif l == w:
    print("It's square")       
