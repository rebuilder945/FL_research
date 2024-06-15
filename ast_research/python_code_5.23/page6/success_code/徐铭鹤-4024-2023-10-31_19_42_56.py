def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       for i in range(a):
            n=a
            s=0
            if n-1>0:
                s=s+10**n+10**(n-1)+10**(n-2)
                n=n-1
       print(s)

           
main()

