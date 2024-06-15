a=eval(input())
b=eval(input())
total=a
qilai=2*a
if b ==1:
    print(a)
else:
    for x in range(1,b,1):
        qilai=qilai*0.5
        total+=qilai
    print("%.2f"%total)
