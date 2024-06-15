def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       s=a
       n=0
      while n<a-1:
             a=a*10+a
             s+=a
             n+=1
      print(s)
main()

