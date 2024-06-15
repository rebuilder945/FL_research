def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    n = 0
    m = a
    while n < a:
        s += m * (10**n) * (a - n)
        n += 1
    print(s)

main()

