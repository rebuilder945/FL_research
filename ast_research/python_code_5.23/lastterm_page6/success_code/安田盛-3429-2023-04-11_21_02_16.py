# a=input()
# x=0
# y=0
# z=0
# haha=[chr(x)for x in range(65,91)]+[chr(x)for x in range(97,123)]
# for i in a:
#     if str.isnumeric(i):
#         x+=1
#     elif str.isspace(i):
#         y+=1
#     elif i in haha:
#         z+=1
# w=len(a)-x-y-z
# b=[z,y,x,w]
# for i in b:
#     print(i,end=" ")


stri=input()
a,b,c,d=0,0,0,0
for i in stri:
    if'a'<=i<='z'or 'A'<=i<='Z':
        a+=1
    elif '0'<=i<='9':
        b+=1
    elif i==' ':
        c+=1
    else:
        d+=1
print(a,c,b,d)
     
