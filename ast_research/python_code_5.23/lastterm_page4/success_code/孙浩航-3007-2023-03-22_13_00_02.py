list1=eval(input())
a,b=eval(input())
if a <= len(list1) and b <= len(list1):
    del list1[a:b]
    print(list1)
elif  a > len(list1) or  b > len(list1):
    print("error")    



