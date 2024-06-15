def main():
    total_count = int(input())
    calculate_days(total_count)
i=0
calculate_days=0
while i<total_count:
    i=(2+i)*2
    calculate_days+=1
print(calculate_days)
main()


