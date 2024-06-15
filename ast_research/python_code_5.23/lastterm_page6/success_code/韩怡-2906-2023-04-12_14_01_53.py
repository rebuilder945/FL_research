def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    import math
    n=0
    while True:
        x=x-math.floor(x/2)-2
        n += 1
        if x<=0:
            break
    print(n)
main()


