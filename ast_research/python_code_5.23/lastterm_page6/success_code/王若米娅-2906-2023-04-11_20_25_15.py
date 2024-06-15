def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count))
def calculate_days(x):
   c=x
   j=0
   while c-int(c/2)-2>0 and c>0:
       j+=1
       c-=int(c/2)-2
   return j

main()


