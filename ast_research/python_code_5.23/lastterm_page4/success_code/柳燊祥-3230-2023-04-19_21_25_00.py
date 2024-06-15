n=eval(input())
n.sort(reverse=True)
if n.count(0)!=len(n):
    for x in n:
        print(x,end="")
else:
    print("0")



