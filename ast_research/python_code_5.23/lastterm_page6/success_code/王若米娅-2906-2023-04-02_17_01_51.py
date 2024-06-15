def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count))
def calculate_days(x):
    c=x
    j=0
    while (c/2-2)%1==0:
        j+=1
        c=c/2-2
    return j
main()


