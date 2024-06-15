lst  =  eval(input())
n,m= eval(input())
if n <= m and m <= len(lst):
    lst1 = lst[n:m:1]
    for i in lst1:
       lst.remove(i)
    print(lst)
else:
    print("error")
