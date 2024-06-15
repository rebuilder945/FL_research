def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       n=1
       q=a
       while n<q:
                s=a*10+q
                a=a*10
                n+=1
                s+=s
                print(s)
       
main()

