def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum = 0
    num = a

    for i in range(a):
        sum += num
        num = num * 10 + a

    print(sum)
main()

