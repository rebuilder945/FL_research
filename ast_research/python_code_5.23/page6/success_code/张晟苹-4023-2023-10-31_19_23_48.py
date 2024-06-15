def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    for i in range(100):
           total_count= total_count-(total_count//2+2)
           if  total_count==0:
               break
    print(i+1)
      
       
main()


