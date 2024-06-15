def is_narcissistic_number(num):
    if num>100:
        num_sum = 0 
        n = len(str(num))
        for i in str(num):
            num_sum += int(i) ** n
        return num_sum == num

n = int(input())

flag = False 

if not flag or n<=100:
    print("none") 
for i in range(1, n + 1):
    if is_narcissistic_number(i): 
        print(i)
        flag = True 



