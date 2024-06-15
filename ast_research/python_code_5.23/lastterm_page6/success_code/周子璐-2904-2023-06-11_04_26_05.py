def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(0,a):
        s=2*s+10**i*a
    print(s)
main()


