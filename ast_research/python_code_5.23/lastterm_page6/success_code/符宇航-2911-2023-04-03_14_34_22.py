n = eval(input())
list11 = list(str(n))
list1 = [int(x) for x in list11]
tt = len(list1)
a = 0
numlist = list(range(tt))
for i in list1:
    qq = (i+5)%10
    numlist[tt-1-a] = qq
    a+=1
print(''.join(map(str,numlist)))

