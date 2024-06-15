list1 = eval(input())
n,m = eval(input())
if n > m or m > len(list1)-1 or n > len(list1)-1:
    print("error")
elif n <= m:
    del list1[n:m]
    print(list1)
