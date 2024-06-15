def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    a=a-(a/2)-2
    a=int(a)
    for i in range(1,a):
        if a>0:
            a=a-int(a/2)-2
        else :
            continue
    print(i)
main()


