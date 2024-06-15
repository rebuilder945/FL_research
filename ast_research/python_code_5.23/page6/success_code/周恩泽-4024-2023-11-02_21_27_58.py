def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       sum=0
       b=a
       for x in range(a):
               sum=a+sum
               a=a*10+b
       print(sum)
main()

