def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e = 1.0
    factorial = 1.0

    for i in range(1, n + 1):
        factorial *= i
        e += 1 / factorial

    return e

# Set the value of n (you can adjust this as needed)
n = 10

result = calculate_e(n)
result_rounded = round(result, 6)

print(f"The estimated value of e with n = {n} is: {result_rounded}")

   
main()


