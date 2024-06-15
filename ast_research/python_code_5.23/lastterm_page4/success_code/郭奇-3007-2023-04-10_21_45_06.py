ls_str = input()
n1,n2 = map(int,input().split(","))
if n1 in ls_str and n2 in ls_str:
    a = ls_str.index(n1)
    b = ls_str.index(n2)
    for i in range(n2-n1-1):
        del ls_str[a+i]
    print(ls_str)
else:
    print(error)
