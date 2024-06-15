import os

a = eval(input())
for file_path in a:
    os.remove(file_path)
    #使用 remove(0) 尝试删除文件或目录，但是 remove() 函数需要传入文件路径（字符串类型）、字节类型或类似路径的对象，而不是整数。
    #如果您想要删除文件列表 a 中的元素，可以使用 os.remove() 函数，并传入文件路径。
    a.append(0)

print(a)