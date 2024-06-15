def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    aa, aasum = 0, 0
    for i in range(1, a+1):
        aa += a * 10**(i-1)
        aasum += aa
    print(aasum)

main()

