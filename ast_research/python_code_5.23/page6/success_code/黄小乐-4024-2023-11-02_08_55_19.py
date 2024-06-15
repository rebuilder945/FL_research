def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        x=str(a)
        l=int(len(x))
        s=0
        n=0
        m=a
        while m>0:
                s=s+a*m*10**n
                m=m-1
                n=n+l
        print(s)
main()

