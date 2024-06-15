def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    c=0
    d=a
    if a<10:
        while c<a:
            b=b+d*a*10**c
            c=c+1
            d=d-1
    else:
        b=10203040506070809100
    print(b)
main()

