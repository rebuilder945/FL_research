def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    if a in range(0,10):
        aa, aasum = 0, 0
        for i in range(1, a+1):
            aa += a * 10**(i-1)
            aasum += aa
        print(aasum)
    else:
        print(10203040506070809100)

main()

