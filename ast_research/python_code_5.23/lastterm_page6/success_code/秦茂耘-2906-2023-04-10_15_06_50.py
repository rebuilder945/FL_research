def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(t):
    day=0
    while(t>0):
        t = t - t//2 - 2
        day+=1
    print(day)
main()


