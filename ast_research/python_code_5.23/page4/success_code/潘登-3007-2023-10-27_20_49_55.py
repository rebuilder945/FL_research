lst=[eval(input())]
n,m=eval(input())
if m not in len(lst) or n not in len(lst):
    print("error")
else:
    lst.remove(lst[n:m])
    print(lst)    
