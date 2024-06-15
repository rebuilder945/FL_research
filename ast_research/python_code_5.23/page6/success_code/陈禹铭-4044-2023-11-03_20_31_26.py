limit=int(input())
armstrong_numbers=[]
for num in range(1,limit+1):
    digits=[int(digit) for digit in str(num)]
    if num==sum(digit**3 for digit in digits):
        armstrong_numbers.append(num)
if armstrong_numbers:
    for number in armstrong_numbers:
        print(number)
else:
    print("none")
