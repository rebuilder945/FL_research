lst = eval(input())
n,m = map(int,input().split(","))
a = len(lst)
if n <= a+1 and m <= a+1:
    lst2 = lst[:n] + lst[m:]
    print(lst2)
  
else:
    print('error')

