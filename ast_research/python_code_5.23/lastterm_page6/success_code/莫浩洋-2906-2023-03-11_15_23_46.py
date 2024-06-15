def main():
    total_count = int(input())
    calculate_days(total_count)
def   calculate_days(x):
         a=0
         while x >0 :
              x=x-0.5*x-2
              a+=1
         print(a)
              
main()


