lst=eval(input())
n,m=eval(input())
if n>m or n>len(lst):
    print('error')
else:
    lst1=lst[:n]+lst[m:]
    print(lst1)
