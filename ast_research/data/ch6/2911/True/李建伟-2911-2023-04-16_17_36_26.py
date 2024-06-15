n = input()
lst = []
for i in list(map(int, n)):
    i = (i+5)%10
    lst.append(i)
lst.reverse()
print(''.join(str(x) for x in lst))

