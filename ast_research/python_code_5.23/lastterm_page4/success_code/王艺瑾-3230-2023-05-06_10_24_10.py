a=eval(input())
if a.count(0)==len(a):
    print(0)
else:
    a.sort(reverse=True)
    for i in a:
        print(i,end="")

            


