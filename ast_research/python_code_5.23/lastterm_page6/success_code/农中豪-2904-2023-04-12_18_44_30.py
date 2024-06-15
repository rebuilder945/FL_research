def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=a
    while n < a :
            if a<10:
                s += m * a * 10**n
                n += 1
                m -= 1
            else:
                s += m * a * 10**(2*n)
                n += 1
                m -= 1
    print(s)
main()

