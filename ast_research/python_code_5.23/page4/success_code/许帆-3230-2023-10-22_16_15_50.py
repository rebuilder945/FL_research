lst1 = eval(input())
lst1.sort(reverse=True)
for i in range(len(lst1)):
    if lst1[i] == 0:
        print(0)
    else:
        print(lst1[i],end='')

