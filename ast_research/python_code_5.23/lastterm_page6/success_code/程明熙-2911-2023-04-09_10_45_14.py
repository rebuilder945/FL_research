# a=input()
# b=[]
# c=''
# for i in range(len(a)):
#     b.append(int(a[i]))
# for i in range(len(b)):
#     b[i]=(b[i]+5)%10
# b.reverse()
# for i in range(len(b)):
#     c+=str(i)
# print(c)

a = input()
c = []
for i in range(len(a)):
    c.append(int(a[i]))
for j in range(len(c)):
    c[j] = (c[j] + 5) % 10
c.reverse()
for k in range(len(c)):
    print(c[k], end='')

