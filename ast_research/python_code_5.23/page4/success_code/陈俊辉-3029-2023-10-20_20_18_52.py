import numbers
from tkinter.font import names


names=list(input())
numbers=list(input())
c=([x+y]for x in names for y in numbers)
print(c)



