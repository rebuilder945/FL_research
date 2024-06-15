from distutils.log import error


lst = input()
a =lst.count
m = eval(input())
n =list(m)
for i in range(n[0],n[1]):
    if n[0]<=a:
        lst.pop(n[0])
        print(lst)
    else:
        print("error")
