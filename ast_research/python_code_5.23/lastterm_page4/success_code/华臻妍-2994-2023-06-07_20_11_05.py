lst = list(map(int,input().split(',')))#map函数不改变原有的list而是返回一个新的list
n,m = eval(input())
if n < len(lst):
    a = lst[n]
    for i in range(m):
        lst.append(a)
    print(lst)
else:
    print("error") # “”可以看12题题目

