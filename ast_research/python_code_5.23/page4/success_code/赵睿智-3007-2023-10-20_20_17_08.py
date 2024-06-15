
lst=input()[1:-1].split(",")
lst=[eval (i) for i in lst ]
n,m=eval(input())
if n>len(lst) or m>len(lst):
        print("error")
elif n<m:
        lst=lst[:n]+lst[m:]
        print(lst)
else:
        lst=lst[:m+1]+lst[n+1:]
        print(lst)






