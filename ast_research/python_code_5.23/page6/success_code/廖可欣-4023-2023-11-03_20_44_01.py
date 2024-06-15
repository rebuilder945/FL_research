def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    x = total_count
    kong = []
    for i in range(x):
        x = x/2 - 2
        if x <= 0:
            pass
        else:
            kong.append(x)
    print(len(kong)+1)
main()


