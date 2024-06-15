def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
    day=1
    while total_count >0:
        total_count=total_count*0.5-2
        if total_count<=0:
            break
        day+=1 
    print(day)
main()


