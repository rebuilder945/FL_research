def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    total = 0
    num = a

    for i in range(a):
        total += num
        num = num * 10 + a

    return total
print(calculate_sum(a))

main()

