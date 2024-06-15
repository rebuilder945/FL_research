def main():
    total_count = int(input())
    calculate_days(total_count)
   print("%d"%calculate_days(total_count))
def calculate_days(total_count):
        i=1
        while (total_count-total_count//2)>2:
                i=i+1
                total_count=total_count-total_count//2-2
        return(i)
main()


