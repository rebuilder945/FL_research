# a = 1
# d={}
# n = input()
# while n!="q" :
#     d[n]=d.get(n,0)+1
#     n=input()
# ls = list(d.items() )
# ls.sort(key = lambda x:x[1],reverse=True)
# print("{} {}".format(ls[0][0],ls[0][1]))

a = list(input().split(" "))
d={}
for i in a:
    d[i]=d.get(i,0)+1
ls = list(d.items() )
ls.sort(key = lambda x:x[1],reverse=True)
max1 = ls[0][1]
for x in ls:
    if x[1]==max1:
        print("{} {}".format(x[0],x[1]))

