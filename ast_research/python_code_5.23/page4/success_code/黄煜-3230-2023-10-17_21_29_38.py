list=eval(input())
list.sort(reverse=True)
for x in list:
    if list[0]==0:
        print(0)
    else:
        print(x,end="")
