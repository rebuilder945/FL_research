def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       a=int(input())
       sum = 0
       for i in range(a):
             sum += int(str(a)*(i+1))
       print(sum)
main()

