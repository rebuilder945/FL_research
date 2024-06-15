def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    total=0
    for x in range(1,a+1,1):
          
          total=total+int((str(a)*x))
    print(int(total))
main()

