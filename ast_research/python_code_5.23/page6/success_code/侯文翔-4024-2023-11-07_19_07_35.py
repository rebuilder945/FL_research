def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
 sum=0
 for x in range(1,a+1):
  sum+=int(str(a)*x)
 print(sum)                     
main()

