def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    count = 0
    while N > 0:
        count += 1
        if N == 1:
            break
        N = N // 2 + 2
    return count

N = int(input())
days = calculate_days(N)
print( days)

main()


