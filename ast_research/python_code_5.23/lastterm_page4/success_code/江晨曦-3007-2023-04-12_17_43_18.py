# #1
# a = input().split(',')
# b = eval(input())
# c = []
# for i in range(len(a)):
#     d = []
#     d.append(a[i])
#     d.append(b[i])
#     c.append(d)
# print(c)

# #2
# a,b,c = eval(input())
# lst = [x for x in range(a,a+b*c,c)]
# print(lst)

#3
a = eval(input())
b,c = list(input())
if b<-len(a) or b>len(a)-1 or c<-len(a) or c>len(a)-1:
    print("error")
elif b<c:
    del a[b,c-1]
else:
    del a[b]
print(a)
