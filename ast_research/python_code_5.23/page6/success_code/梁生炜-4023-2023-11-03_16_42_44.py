def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
       d=0
       while total_count>0:
               d+=1
               w=total_count//2+2
               total_count-=w
       print(d)
main()


