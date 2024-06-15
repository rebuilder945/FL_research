def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n = 0
    for i in range(1,a+1):                    #2     2+22
          temp = 0
          for j in range(i):
                temp = temp + a*10**j
          n = n + temp
        
    print(n)
main()

