def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
            m=a
            s=0
            n=0
            while n<a:
                     s=s+m*a*10**n
                     n=n+1
                     m=m-1
            print(s)

           
main()

