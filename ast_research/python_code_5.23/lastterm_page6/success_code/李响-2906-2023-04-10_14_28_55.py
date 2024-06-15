def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
      x = 0
      while (total_count/2-2)>0:
         x = x + 1
         total_count = int(total_count/2-2)
      print(x+1)
main()


