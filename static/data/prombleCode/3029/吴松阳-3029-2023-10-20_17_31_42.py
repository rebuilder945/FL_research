a = input().split(',')
b = eval(input())
lst = []
for i in range(len(b)):
    lst.extend([[a[i],b[i]]])
print(lst)
