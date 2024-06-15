def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    sum=0
    for i in range(a):
        a = a + a*(10**i)
        sum = sum + a
    return sum
main()

