str = input()
a = str.split(' ')
# print(a)
num = input()
b = num.split()
a[b[0]], a[b[1]] = a[b[1]], a[b[0]]
print(a)
