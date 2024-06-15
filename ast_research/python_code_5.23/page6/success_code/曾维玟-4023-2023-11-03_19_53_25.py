def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
 i = 0
while total_count>0:
 total_count = int(total_count/2+2)
 i = i+1
print(i)
main()


