def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=(10**a - 1) * a * (10 - a)
    print(s)
main()

