number = list(input())              #将字符串中的每个字符都化为列表中的一个元素
for i in range(len(number)):
    number[i] = (int(number[i])+5)%10
number = number[::-1]
number = "".join(map(str,number))
print(number)
