def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1.0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        e += 1 / factorial
    print(f"{e:.6f}")

main()


