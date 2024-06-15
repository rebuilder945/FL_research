def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
   for x in range(total_count/2):
      if (total_count/2-2)<=0:
         print(x+1)
      else:
         total_count = int(total_count/2-2)
main()


