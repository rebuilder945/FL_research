def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=a
    if a!=10:    
        while n < a :
            s += m * a * 10**n
            n += 1
            m -= 1
        print(s)
    else:
        s=10203040506070809100    
        print(s)
main()

