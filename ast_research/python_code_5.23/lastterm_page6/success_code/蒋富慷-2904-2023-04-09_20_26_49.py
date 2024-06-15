def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = 0
    c = a
    while a > 0:
        for i in range(a):
            b =b + c*10**i
            a = a-1
    print(b)
main()

