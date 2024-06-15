def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    count=0
    day=0
    while count<x:
        day+=1
        if day==1:
            count+=x//2+2
        else:
            count+=(count//2)+2
    print(day)
main()


