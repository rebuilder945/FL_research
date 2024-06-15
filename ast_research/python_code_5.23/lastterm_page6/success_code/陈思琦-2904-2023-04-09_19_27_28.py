def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=[]
        for i in range(0,a+1):
            d=a-i
            c=10**i*d*a
            b.append(c)
        print(sum(b))
main()

