numbers=eval(input())
numbers1=[]
for i in numbers:
    if numbers.count(i)==1:
        numbers1.append(i)
if numbers1==[]:
    print("False")
else:
    numbers1.sort()
    print(numbers1)
