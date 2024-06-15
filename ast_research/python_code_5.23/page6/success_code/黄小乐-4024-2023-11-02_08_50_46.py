def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        s=0
        n=0
        m=a
        if a<10:
            while n<a:
                s=s+a*m*10**n
                m=m-1
                n=n+1
        else:
            while n<a:
                s=s+a*m*10**n
                m=m-1
                n=n+6
        print(s)
main()

