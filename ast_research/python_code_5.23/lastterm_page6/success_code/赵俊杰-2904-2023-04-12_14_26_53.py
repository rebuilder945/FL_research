def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=1
    s=0
    n=a
    while n>0:
        s=s+a*x*10**(a-1)
        n=n-1
        x=x+1
    print(s)
main()

