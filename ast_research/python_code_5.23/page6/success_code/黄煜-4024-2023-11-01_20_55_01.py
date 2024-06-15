def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    if a>9:
         print("10203040506070809100")
    else:
        s=0
        n=0
        m=a
        while n < a :
            s += m * a * 10**n
            n += 1
            m -= 1
        print(s)

main()

