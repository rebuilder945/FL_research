from distutils.log import error


lst = input()
a =lst.count
m = eval(input())
n =list(m)
b =n[0]
for i in range(b,n[1]):
    if b<a:
        lst.pop(n[0])
        print(lst)
    else:
        print("error")
