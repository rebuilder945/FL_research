def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(y):
    Sum = 0
    for i in range(1, y + 1):
        x = int(str(y) * i)
        Sum += x
    print(Sum)
main()

