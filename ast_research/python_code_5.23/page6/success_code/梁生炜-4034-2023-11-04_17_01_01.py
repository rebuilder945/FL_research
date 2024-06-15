a=input().split()
b=input().split()
th=['red','blue','yellow']
if a==b or a[0] not in th or b[0] not in th:
    print("error")
elif a[0]==th[0]:
    if b[0]==th[1]:
        print('purple')
    else:
        print('orange')
elif a[0]==th[1]:
    if b[0]==th[0]:
        print('purple')
    else:
        print('green')
else:
    if b[0]==th[0]:
        print('orange')
    else:
        print('green')
