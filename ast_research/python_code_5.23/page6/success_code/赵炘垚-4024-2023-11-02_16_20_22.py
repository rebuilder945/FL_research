def main():
    a=int(input())
    calculate_sum(a)

def calculate_sum(a):
    item_generator=[int("".join([str(a)]*i)) for i in range(1,a+1)]
    print(sum(item_generator))

main()

