def main():
    total_count = int(input())
    calculate_days(total_count)
       while total_count > 0:
              days(total_count)+=1
              total_count=total_count//2+2
       print(days(total_count))
main()


