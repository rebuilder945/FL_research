def main():
    total_count = int(input())
    calculate_days(total_count)
n=0
while total_count > 0:
        n+=1
        total_count=total_count//2+2
print(n)
main()


