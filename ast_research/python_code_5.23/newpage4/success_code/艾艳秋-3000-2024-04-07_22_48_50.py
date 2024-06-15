def jia(list1):
    b=0
    for x in list1:
        b=x+b
    c=b/len(list1)
    print("%.2f"%c)    
a=eval(input())
jia(a)
