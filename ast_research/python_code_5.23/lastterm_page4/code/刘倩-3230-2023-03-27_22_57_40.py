n = eval(input())
if all(x!=0 for x in b):
    n.sort(reverse=True)
a = [str(x) for x in n]
b = ''.join(a)
    print(b)
else:
    print("0")
