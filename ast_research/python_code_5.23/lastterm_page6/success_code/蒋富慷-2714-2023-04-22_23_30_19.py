a = {1:'A',2:'B',3:'C',4:'D',5:'E'}
b = eval(input())
if b >= 90:
    print(a[1])
elif b >= 80:
    print(a[2])
elif b >= 70:
    print(a[3])
elif b >= 60:
    print(a[4])
else:
    print(a[5])
