def shuixian(n):
    list1=[]
    for x in n:
        list1.append(int(x))
    if list1[0]**3+list1[0]**3+list1[0]**3==int(n):
        return True
    else:
        return False
n=input()
for x in range(100,int(n)+1):
    if shuixian(n):
        print(n)
else:
    print('none')

