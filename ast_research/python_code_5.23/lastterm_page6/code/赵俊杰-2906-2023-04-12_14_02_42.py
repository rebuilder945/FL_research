def main():
    total_count = int(input())
    calculate_days(total_count)
       x=0
        while total_count>0:
              if total_count%2==0:
                    total_count=total_count/2-2
                    x=x+1
              else:
                    total_count=(total_count+1)/2-2
                    x=x+1
         print(x)
main()


