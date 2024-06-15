def main():
    total_count = int(input())
    calculate_days(total_count)
def days_to_sell_all(N):
    count = 0
    while N > 0:
        count += 1
        if N == 1:
            break
        N = N // 2 + 2
    return count

N = int(input())
days = days_to_sell_all(N)
print( days)

main()


