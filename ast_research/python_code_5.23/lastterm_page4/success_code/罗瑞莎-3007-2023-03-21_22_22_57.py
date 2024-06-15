lst = eval(input())
s = input()
n,m = eval(s)
if m<=len(lst):
    for i in range(m-n):
        del lst[n]
    print(lst)
else:
    print("error")
