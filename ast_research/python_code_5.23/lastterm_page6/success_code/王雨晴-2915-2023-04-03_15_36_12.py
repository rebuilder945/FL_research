def is_narcissistic_number(n):
    n_str = str(n)
    length = len(n_str)
    return n == sum(int(digit) ** length for digit in n_str)

def main():
    n = int(input())
    found = False
    for i in range(10, n+1):
        if is_narcissistic_number(i):
            found = True
            print(i)
    if not found:
        print("none")

if __name__ == '__main__':
    main()

