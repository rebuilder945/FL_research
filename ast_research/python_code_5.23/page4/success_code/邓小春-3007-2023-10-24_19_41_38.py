from ast import Del


l=input()
list(l)
n,m=eval(input())
if n>len(l) and m>len(l):
    print("error")
else:
    l.remove(n,m)
    print(l)
