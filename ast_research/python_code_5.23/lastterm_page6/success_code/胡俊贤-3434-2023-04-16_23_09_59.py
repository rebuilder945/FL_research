pri1=input()
pri2=input()
if pri1=='red' and pri2=='blue' or pri1=='blue' and pri2=='red':
    print('purple')
elif pri1=='red' and pri2=='yellow' or pri1=='yellow' and pri2=='red':
    print('orange')
elif pri1=='blue' and pri2=='yellow' or pri1=='yellow' and pri2=='blue':
    print('green')
else:
    print("error")
