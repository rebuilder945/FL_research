def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
       lst = [1]
       x = 0
       for i in range(n):
            x+=1
            lst.append(1/x!)
       print("%.6f"%sum(lst))
main()


