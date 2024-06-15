lst=[eval(input())]
n,m=eval(input())
if m>len(lst) or n>len(lst):
    print("error")
else:
    lst.remove(lst[n:m])
    print(lst)    
