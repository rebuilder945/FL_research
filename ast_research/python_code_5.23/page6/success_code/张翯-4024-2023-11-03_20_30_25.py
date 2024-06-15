def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       s=0
       for a in range(a):
              s+=a
              a=a*10+a
       print(s)
main()

