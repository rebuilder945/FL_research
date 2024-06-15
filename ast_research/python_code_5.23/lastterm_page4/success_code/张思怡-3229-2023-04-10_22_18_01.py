a=eval(input())
# # if 1==min([a.count(x) for x in a]):
# #     del a[x]
# #     print(a)    
# b=[a.count(x) for x in a]
# for i in range (len(a)):
#     if b[i]==1:
#         print(i)
        
#         # del a[i]
#         # continue
# 
# # print(a)
# # c=b.index(1,0)
# # print(c)
c=set(a)
b=[]

for i in c:
    if(a.count(i)==1):
        b.append(i)
b.sort()
if(b==[]):
    print("False")
else:
    b=list(map(str,b))
    print(",".join(b))
