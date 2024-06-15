def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    total = 0
    num = 0
    for i in range(1, a+1):
        num = num * 10 + a
        total += num
    return total
main()

