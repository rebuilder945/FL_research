#把列表中的各位整数组合成一个最大的整数
#将数字转化为字符串，字符串的加减是直接拼合
from audioop import reverse


l = eval(input())
l.sort(reverse=True)
print(*l,sep="")
