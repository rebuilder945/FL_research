def main():
    total_count = int(input())
    calculate_days(total_count)
       count=0       
       while total_count>0:
              count+=1
              total_count=total_count//2+2
       days(total_count)=count
       print(days(total_count))
main()


