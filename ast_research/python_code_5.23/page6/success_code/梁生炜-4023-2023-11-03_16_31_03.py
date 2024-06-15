def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
       d=0
       w1=total_count//2+2
       w2=total_count-w1
       while w2!=0:
                 d+=1
                 w1=total_count//2+2
                 w2=total_count-w1
       print(d)
main()


