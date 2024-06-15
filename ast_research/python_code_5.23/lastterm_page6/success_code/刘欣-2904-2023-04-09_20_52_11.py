def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum = 0
    current = a
    for i in range(a):
        sum += current
        current = current * 10 + a
        current = current // 10
    print(sum)
main()

