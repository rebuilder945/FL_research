from distutils.log import error


lst = input()
a =lst.count
m = eval(input())
n =list(m)#n=m[0]m=m[1]
for i in range(m[0],m[1]):
    if m[0]<a:
        lst.pop(m[0])
        print(lst)
    else:
        print("error")
