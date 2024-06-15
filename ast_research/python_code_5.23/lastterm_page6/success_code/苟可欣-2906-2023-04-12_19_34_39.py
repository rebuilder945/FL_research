def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total):
    for x in range(100):
        total=total/2 -2
        if total==0:
            print(x+1)
            break
        elif total<1:
            print(x+2)
            break
        else:
            continue

main()


