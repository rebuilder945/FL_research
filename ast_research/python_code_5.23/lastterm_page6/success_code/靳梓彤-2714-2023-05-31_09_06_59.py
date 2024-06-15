grade=eval(input())
if grade>=90:
    level='A'
elif grade>=80 and grade<90:
    level='B'
elif grade>=70 and grade<80:
    level='C'
elif grade>=60 and grade<70:
    level='D'
else:
    level="E"
print(level)

