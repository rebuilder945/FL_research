a = input()
a = list(a)
b = eval(input())
c = [[a[x]+b[x]] for x in range(len(a))]
