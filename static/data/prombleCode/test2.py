import json
import os
import shutil
import requests
import json
from openpyxl import Workbook

# with open("/home/wsy/python机器人数据/code-demo/data/prombleCode/error.json", 'r') as f:
#     error = json.load(f)

def select_error(error:dict) -> list:
    outrange = []

    for key in error:
        error_info = error[key]
        if "list index out of range" in error_info:
            outrange.append(key)
    return outrange

# 将目标python文件复制到目标文件夹
def copy_python_files(source_dir, target_dir, file_list):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for filename in file_list:
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        shutil.copyfile(source_file, target_file)
        print(f"File '{filename}' copied to '{target_dir}'")

# 将目标文件构造成prompt批量询问gpt
def ask_api(prompt):
    url = "https://oa.api2d.net/v1/chat/completions"

    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "safe_mode": False
    })
    headers = {
    'Authorization': 'Bearer fk216618-f39L8P2msSmhydRuG51oDh1aDG0CklUV',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

if __name__ == "__main__":
    # source_directory = "/home/wsy/python机器人数据/code-demo/data/prombleCode/3029"
    # target_directory = "/home/wsy/python机器人数据/code-demo/data/prombleCode/outrange"
    # outrange = select_error(error)  
    # copy_python_files(source_directory, target_directory, outrange)

    # 设置文件路径和文件名
    excel_file = "D:\\CQU\\项目\\python机器人数据\\prombleCode\\output.xlsx"

    # 创建一个 Excel 工作簿
    wb = Workbook()
    ws = wb.active

    # 添加表头
    ws.append(["文件名", "代码", "gpt回答"])

    code_file = "D:\\CQU\\项目\\python机器人数据\\prombleCode\\outrange"

    with open("D:\\CQU\\项目\\python机器人数据\\prombleCode\\error.json", encoding="utf-8") as f:
        error = json.load(f)

    question = '''

    【问题描述】

    已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。要求，把姓名和对应的成绩进行组合，形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。最后输出形成的新列表。
    【输入形式】

    分两行输入，第一行输入姓名，按照字符串的方式输入，多个姓名之间用逗号分隔。第二行输入成绩，包含方括号，元素之间用英文逗号分隔。
    【输出形式】

    直接用print输出新的列表。
    【样例输入】

    tom,jack,jone,mike

    [88,89,34,90]
    【样例输出】

    [['tom', 88], ['jack', 89], ['jone', 34], ['mike', 90]]

    【样例说明】

    把两个单独的列表合并成嵌套列表。
    '''

    for code_name in os.listdir(code_file):
        code_path = os.path.join(code_file,code_name)
        with open(code_path, encoding="utf-8") as c:
            code = c.read()
        error_info = error[f"{code_name}"]
        prompt = "题目描述为：\n" + question \
                 +"\n我的代码为:\n" + code \
                 +"\n我代码出现的报错信息为:\n" + error_info \
                 +"\n指出我的代码存在的错误是什么,我该如何修改我的代码?" 
        response = ask_api(prompt)
        reslut = json.loads(response.text)
        answer = reslut["choices"][0]["message"]['content']
        # 将文件名、代码和回答内容写入 Excel 表格 
        ws.append([code_name, code, answer])
        print(f"{code_name}已记录")
    wb.save(excel_file)
