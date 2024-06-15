a=input("")
b=input("")
ls=["red","blue","yellow"]
if a==ls[0]and b==ls[1]or a==ls[1] and b==ls[0]:
    print('purple')
elif a==ls[0] and b==ls[2]or a==ls[2] and b==ls[0]:
    print('orange')
elif a==ls[1] and b==ls[2]or a==ls[2]and b==ls[1]:
    print('green')
else:
    print('error')

