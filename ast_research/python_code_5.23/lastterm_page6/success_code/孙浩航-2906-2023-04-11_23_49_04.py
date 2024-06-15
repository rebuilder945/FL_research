def main():
    total_count = int(input())
    calculate_days(total_count)
def   calculate_days(total_count):
        day=0
        while total_count>0:
            total_count=total_count//2-2
            day=day+1
            if total_count<2:
                day=day+1
            return(print(day))

main()


