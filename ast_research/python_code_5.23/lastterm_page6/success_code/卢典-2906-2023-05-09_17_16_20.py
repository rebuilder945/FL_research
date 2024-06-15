def main():
    total_count = int(input())
    calculate_days(total_count)
n=0
m=total_count
while m > 0:
         n+=1
         m=m//2+2
print(n)
main()


