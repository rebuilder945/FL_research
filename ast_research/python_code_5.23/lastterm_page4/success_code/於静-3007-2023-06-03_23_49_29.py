lst=eval(input())
n,m=eval(input())
if n>0 and n<=m and m<len(lst):
    list=lst[0:n]+lst[m:len(lst)]
    print(list)
else:
    print("error")

