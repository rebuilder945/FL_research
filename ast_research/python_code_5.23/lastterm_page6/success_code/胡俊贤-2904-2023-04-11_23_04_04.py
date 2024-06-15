def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    for i in range(a):
        sum = sum + a
        a = a + a*10**i
    return sum
main()

