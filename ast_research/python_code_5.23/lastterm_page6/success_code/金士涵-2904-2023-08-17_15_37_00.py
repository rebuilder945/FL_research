def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       n=1
       q=a
       while n<a:
                s=a*10+q
                a=a*10
                n+=1
                print(s)
       
main()

