ls = eval(input())
a = min(ls)
b = max(ls)
while a in ls:
    ls.remove(a)
while b in ls:   
    ls.remove(b)
print(ls)
