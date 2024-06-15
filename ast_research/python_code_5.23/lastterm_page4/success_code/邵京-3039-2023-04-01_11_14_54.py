numbers=eval(input())
maxnumber=max(numbers)
minnumber=min(numbers)
while numbers.count(maxnumber)>0:
    numbers.remove(maxnumber)
while numbers.count(minnumber)>0:
    numbers.remove(minnumber)
print(numbers)
