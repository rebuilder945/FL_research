lst1 = eval(input())
lst1.sort(reverse=True)
if lst1[0] == 0:
    print(0)
else:
    for i in range(len(lst1)):
        print(lst1[i],end='')

