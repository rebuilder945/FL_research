a=eval(input())
m=100
s=[]
for i in range(100,a+1):
    si=str(i)
    si1=int(si[0])
    si2=int(si[1])
    si3=int(si[2])
    if i==si1**3+si2**3+si3**3:
        s.append(i)
if len(s)==0:
    print("none")
if len(s)!=0:
    for x in s:
        print(x)
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
