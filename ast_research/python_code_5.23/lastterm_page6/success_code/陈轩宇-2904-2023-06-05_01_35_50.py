def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       sum1 = a
       while a<a*10**(a-1):
              save=[]
              sum1+=a*10
              a = a*10
              save.append(sum1)
       b = sum(save)
       print(b)
main()

