def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
      M=0
      while  total_count>0:
                total_count=total_count-(total_count/2+2)
                M+=1
      print(M)
                
               
                
main()


