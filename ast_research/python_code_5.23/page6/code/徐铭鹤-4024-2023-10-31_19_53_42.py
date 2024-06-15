def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
            n=a
            s=0
            m=0
            while m<a:
                     s=s+n*a*10**n
                     n=n-1
                     m=m+1
       print(s)

           
main()

