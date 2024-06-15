# c=["red","blue",'yellow']
# a=input()
# b=input()
# if a not in c or b not in c:
#     print("error")
# elif a==b:
#     print("error")
# else:
#     if (a==c[0] and b==c[1])or (a==c[1]and b==c[0]):
#         print("purple")
#     elif(a==c[0] and b==c[2])or (a==c[2]and b==c[0]):
#         print("orange")
#     elif(a==c[1] and b==c[2])or (a==c[2]and b==c[1]):
#         print("green")
c={"red","blue",'yellow'}
a=input()
b=input()
if (a not in c) or (b not in c)or a==b :
    print("error")
else:
    d={a,b}
    if d=={"red",'blue'}:
        print('purple')
    elif d=={'red','yellow'}:
        print('orange')
    else:
        print('green')



