a = input()
b = input()
s1 = {a,b}
c1 = {"blue",'red'}
c2 = {'blue','yellow'}
c3 = {'red','yellow'}
if s1 == c1:
    print("purple")
elif s1 == c2:
    print("green")
elif s1 == c3:
    print('orange')
else:
    print('error')

