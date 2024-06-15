def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(dy):
    a = 0
    while dy > 0:
        dy = dy/2-2
        a+=1
    print(a)
main()


