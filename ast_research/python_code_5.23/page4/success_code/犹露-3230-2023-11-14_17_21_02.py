a = eval(input())
a.sort(reverse=True)
if sum(a)==0:
        print(0)

for i in a:
        print(i,end="")
