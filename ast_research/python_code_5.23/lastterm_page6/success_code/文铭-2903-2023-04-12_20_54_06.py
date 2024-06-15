def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
       lst = [1]
       x = 0
       p = 1
       for i in range(n):
            x+=1
            for m in range(1,x):
                p=p*(m+1)
            lst.append(1/p)
       print("%.6f"%sum(lst))
main()


