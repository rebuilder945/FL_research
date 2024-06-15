def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
   N=input()
   i = 0
   while N > 0:
   N -= int(N/2)+2
   i = i + 1
print(i)
main()


