def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    sum=0
    n=a
    for i in range(1,a+1):
        sum = sum + a
        a = a + n*(10**i)
    return sum
main()

