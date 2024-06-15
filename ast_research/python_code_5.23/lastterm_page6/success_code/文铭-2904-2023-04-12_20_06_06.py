def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       s = [a]
       for i in range(a-1):
            s.append(10*s[-1]+a)
       print(sum(s))
       
main()

