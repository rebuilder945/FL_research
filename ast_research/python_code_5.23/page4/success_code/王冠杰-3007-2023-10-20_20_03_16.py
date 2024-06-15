lst=eval(input())
n,m=input().split(',')
if n<len(lst) and m<len(lst) :
    if n<m :
        del lst[n:m]
        print(lst)
else :
    print('error')
        


