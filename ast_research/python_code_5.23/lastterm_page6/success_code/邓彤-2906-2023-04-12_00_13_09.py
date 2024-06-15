def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
      for x in total_count:
           while x >0:
                i=0
                a=(x/2)+2
                total_count=x-a
                i+=1
print(i)
main()


