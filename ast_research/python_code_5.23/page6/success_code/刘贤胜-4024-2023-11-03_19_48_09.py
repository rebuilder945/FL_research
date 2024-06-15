def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    b=0
    for x in range(a):
        n=10**x
        b=a*n+b
        s=s+b
    print(s)
main()

