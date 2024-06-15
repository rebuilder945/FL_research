a=eval(input())
ch=len(str(a))
m=10**(ch-1)
for i in range(m,a):
    i=str(i)
    ch1=len(i)
    s=0
    for x in range(0,ch1-1):
        s+=int(i[x])**ch
        if i==s:
            print(i)
    ch1=ch1-1
else:
            print("none")
# m=10**(weishu-1)
# n=10**weishu
# l1=[]
# l2=[]
# l3=[]
# x=0
# y=weishu
# def s(num):
#     return num**a
# for i in range(m,n):
#     l1.append(i)
#     i=str(i)
#     for c in range(0,weishu):
#         b=int(i[c])
#         l2.append(b)
# s=list(map(str,l2))
# for j in range(0,int((len(s)/weishu))):
#     z=sum(s[0:weishu])
#     l3.append(z)
#     x=x+a
#     y=y+a
# for z in range(len(l3)):
#     if l2[z]==l3[z]:
#         print(l2[z])
# else:
#     print("none")
