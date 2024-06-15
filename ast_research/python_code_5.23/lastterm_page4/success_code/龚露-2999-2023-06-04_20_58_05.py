a = input()
ls = a.split()
b,c = eval(input())
ls[b],ls[c]=ls[c],ls[b]
print(ls)
