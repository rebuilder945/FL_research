# a = eval(input())
# for b in range(a):
#     c = b[0]
#     b.remove(c)
#     b.qppend(c)
#     break
# print(b)


n = eval(input())
a = list(range(1,n+1))
b = list(a[1:n+1])
c = a[0]
b.append(c)
print(b)





