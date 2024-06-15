def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
     s = 0
     num = str(a)
     temp = num
     for i in range(a):
          s += int(temp)
          temp += num
     print(s)

main()

