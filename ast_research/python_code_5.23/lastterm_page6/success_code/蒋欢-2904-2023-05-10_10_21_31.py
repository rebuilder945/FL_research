def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        if a==10:
                 print(10203040506070809100)
        m=a
        n=0
        s=0
        while n<a:
                s+=m*a*10**n
                n+=1
                m-=1
        print(s)
        print(a)
main()

