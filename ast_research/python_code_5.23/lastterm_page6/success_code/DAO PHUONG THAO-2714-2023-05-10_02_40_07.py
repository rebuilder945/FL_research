score=eval(input())
if score>=90:
   Level='A'
elif score>=80 and score<90:
   Level='B'
elif score>=70 and score<80:
   Level='C'
elif score>=60 and score<70:
   Level='D'
else:
   Level='E'
print(Level)
