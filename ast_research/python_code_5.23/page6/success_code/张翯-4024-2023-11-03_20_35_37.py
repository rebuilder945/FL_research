def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       s=a
       for a in range(a-1):
             a=a*10+a
             s+=a
       print(s)
main()

