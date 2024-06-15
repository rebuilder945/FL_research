list=eval(input())
n,m=eval(input())
if n in range(len(list)) and m in range(len(list)):
    for x in range(n,m):
        del list[x]
    print(list)
else:
    print('error')
