list = eval(input())
list.sort(reverse=True)
b = [str(x)for x in list]
c = ''.join(b)
d = int(c)
print(d)
