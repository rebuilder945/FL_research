a=eval(input())
S=''
if a>=90:
    S='A'
elif a<90 and a >=80:
    S='B'
elif a<80 and a >=70:
    S='C'
elif a<70 and a >=60:
    S='D'
else:
    S='E'
print(S)
