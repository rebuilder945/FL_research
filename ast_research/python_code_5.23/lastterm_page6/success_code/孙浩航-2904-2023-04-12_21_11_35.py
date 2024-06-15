def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    d=0
    for i in range(0,a):
        c=a*10**i
        b=b+c
        d=b+d
    print(d)
main()

