def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=a
    while n < a and a<10:
        s +=m*(a*10**n)
        n += 1
        m -= 1
    if a==10:
       s=10203040506070809100
    print(s)
main()

