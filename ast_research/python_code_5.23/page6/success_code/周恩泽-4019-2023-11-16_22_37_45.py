n1=input()
n2=[]
for x in n1:
    b=(int(x)+5)%10
    n2.append(b)
n2.reverse()
print("".join(str(x) for  x in n2))


# n=eval(input())
# a=[]
# for x in str(n):
#     x=(int(x)+5)%10
#     a.append(x)
# a.reverse()
# print("".join(str(x) for x in a))

