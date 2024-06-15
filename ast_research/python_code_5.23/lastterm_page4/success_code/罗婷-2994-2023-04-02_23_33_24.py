lst=eval(input())
n,m=eval(input())
lst=list(lst)

if n>=len(lst) or n<(-len(lst)):
    print("error")
else:
    repeat_num=lst[n]
    for i in range(m):
        lst.append(repeat_num)
    print(lst)
