def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=a
    while a>n:
        s=s+m*a*(10**n)
        m=m-1
        n=n+1
    print(s)
main()

