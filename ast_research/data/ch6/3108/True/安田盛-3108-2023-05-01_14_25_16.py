# a=eval(input())
# b=''
# for i in a:
#     b+=i
# c=[chr(x) for x in range(97,123)]
# d=""
# for i in c:
#     d+=i
# for x in d:
#     e=b.count(x)
#     if b.count(x)!=0:
#         print("%s,%.d"%(x,e))
n=eval(input())
s=""
for i in n:
    s=s+i

dic={}
for i in s:
    dic[i]=dic.get(i,0)+1
lis=[]
for x,y in dic.items():
    lis.append([x,y])
lis.sort(key=lambda x:x[0])
for i in range(len(lis)):
    print(lis[i][0],lis[i][1],sep=",")


    
