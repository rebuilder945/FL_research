def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
   jishu=0
   while x>0:
       x=x-int(x/2)-2
       jishu+=1
   print(jishu)
main()


