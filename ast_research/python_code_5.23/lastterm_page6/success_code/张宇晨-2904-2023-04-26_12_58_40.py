def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    b=a
    for i in range(1,a+1):
        sum = sum + b
        b = b + a*10**i
    print(sum)
main()

