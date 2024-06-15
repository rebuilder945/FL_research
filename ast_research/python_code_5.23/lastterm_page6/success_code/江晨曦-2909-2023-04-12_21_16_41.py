# #1
# a = input()
# b = ""
# for i in a:
#     if (int(i)+5)%10 !=0:
#         b = b+str((int(i)+5)%10)
#     else :
#         b = b+"0"
# b= b[::-1]
# print(b)

#2
a =eval(input())
b =eval(input())
s = a
for i in range(b-1):
    s+= a/2**i
print('%.2f'%s)
