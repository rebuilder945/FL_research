n=eval(input())
if n>=90:
    L="A"
elif n>=80 and n<90:
    L="B"
elif n>=70 and n<80:
    L="C"
elif n>=60 and n<=70:
    L="D"
else:
    L="E"
print(L)
