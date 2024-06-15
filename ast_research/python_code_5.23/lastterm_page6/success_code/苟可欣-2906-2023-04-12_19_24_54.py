def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total):
    for x in range(100):
        total=int(total/2-2)
        if total==0:
            print(x+1)
            break
        else:
            continue
main()


