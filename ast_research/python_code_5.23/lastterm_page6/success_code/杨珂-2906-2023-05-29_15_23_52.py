def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    i=0
    while a>1/2:
        a=a-a*1/2-2
        i=i+1
print(i)

main()


