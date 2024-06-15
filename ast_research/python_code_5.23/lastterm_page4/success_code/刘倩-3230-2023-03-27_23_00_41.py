n = eval(input())
n.sort(reverse=True)
a = [str(x) for x in n]
b = ''.join(a)
if all(x==0 for x in n): 
    print("0")
else:
    print(b)
