n=eval(input())
n.sort(reverse=True)
if n[0]!=0:
    for x in n:
        print(x,end="")
else:
    print('0')
