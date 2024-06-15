sums = eval(input())
lst = [0]
x = sums.count(0)
while 0 in sums:
    sums.remove(0)
lst1=sums+lst*xprint(lst1)
