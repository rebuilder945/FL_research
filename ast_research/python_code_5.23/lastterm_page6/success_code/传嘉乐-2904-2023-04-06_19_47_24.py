def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    t=a
    n=a
    while n>0 and a<10:
        s+=t
        a*=10
        t+=a
        n-=1
        print(s)
    while a>10:
        print('10203040506070809100')
main()

