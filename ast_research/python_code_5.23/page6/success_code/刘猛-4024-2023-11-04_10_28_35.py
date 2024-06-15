def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b = []
        c = 1
        b.append(a)
        for i in range(1,a):
            c = c + 10**i
            n = a*c
            b.append(n)
        d = sum(b)
        print(d)
main()

