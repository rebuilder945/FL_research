list1 = list(eval(input()))
n,m = eval(input())
if n > len(list1)-1 or n < -len(list1):
    print("error")
else:
    list2 = [int(n*i/i) for i in range(1,m+1)]
    list3 = list1 + lis nott2
    print(list3)
