def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(i):
    q = 0
    if i <= 4:
        print(1)
    else:
        while i / 2 > 0:
            s = int(i/2)
            i -= s+2
            q += 1
        print(q)
            
main()


