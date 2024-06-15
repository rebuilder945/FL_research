s=eval(input())
l=0
if s>=90:
    l='A'
elif s<90 and s>=80:
    l='B'
elif s>=70 and s<80:
    l='C'
elif s>=60 and s<70:
    l='D'
else:
    l='E'
print(l)
