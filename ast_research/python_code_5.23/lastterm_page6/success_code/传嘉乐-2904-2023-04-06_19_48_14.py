def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    t=a
    n=a
    if  a<10:
        while n>0 :
            s+=t
            a*=10
            t+=a
            n-=1
            print(s)
    else:
        print('10203040506070809100')
main()

