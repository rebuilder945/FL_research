import json
import os
import shutil
import requests
import json

with open("/home/wsy/python机器人数据/code-demo/data/prombleCode/error.json", 'r') as f:
    error = json.load(f)

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
    prompt = '''我这段代码的问题在哪：a = list(input())
                b = list(input())
                for i in range(len(a)):
                    c = []
                    c.append(a[i])
                    c.append(b[i])
                print(c)
                '''
    response = ask_api(prompt)
    print(type(response))

