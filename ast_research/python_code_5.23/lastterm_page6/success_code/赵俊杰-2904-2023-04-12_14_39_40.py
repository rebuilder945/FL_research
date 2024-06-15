def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=1
    s=0
    n=a
    m=a//10
    if m==0:
        while n>0:
            s=s+a*x*10**(n-1)
            n=n-1
            x=x+1
    else:
        while n>0:
            s=s+a*x*10**((n-1)*2)
            n=n-1
            x=x+1
    print(s)
main()

