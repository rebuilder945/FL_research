def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count:int):
    res = 0
    while total_count>0:
        sell = (total_count//2+2)
        total_count -= sell
        res += 1
    print(res)
main()


