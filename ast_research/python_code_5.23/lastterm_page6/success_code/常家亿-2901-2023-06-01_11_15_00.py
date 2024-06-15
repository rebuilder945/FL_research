lst = []
while True:
    s = input()
    if s == '#':
        break
    lst.append(s)
lst1 = list(map(int,lst))
m = sum(lst1)
n = len(lst1)
print("%d %d"%(n,m))

 
