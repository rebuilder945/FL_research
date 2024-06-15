lst=input().split()
a,b=eval(input())
lst[a-1],lst[b-1]=lst[b-1],lst[a-1]
print(lst)
