def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
       y=0
       while x>0:
              x=x-x//2+2
              y+=1
      print(y)
main()


