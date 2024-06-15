def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count))
def calculate_days(x):
    j=0
    while True:
        if x%2==0:
            x=x/2-2
            j+=1
        if x%2==1:
            x=x-(x-1)/2-2
            j+=1
        if x<=0:
            break
    return j

main()


