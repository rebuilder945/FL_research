import xml.etree.ElementTree as ET
import subprocess
import json
import os


def parse_test_cases(xml_file):
    test_cases = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for test_data in root:
        if test_data.tag.startswith('testData'):
            input_data = test_data.find('input').text.strip()
            output_data = test_data.find('output').text.strip()
            test_cases.append((input_data, output_data))
    return test_cases

def run_python_code(code, input_data, timeout=10):
    try:
        with subprocess.Popen(['python', '-c', code], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            try:
                stdout, stderr = process.communicate(input=input_data, timeout=timeout)
                return stdout.strip(), stderr.strip()
            except subprocess.TimeoutExpired:
                process.kill()
                return None, "Timeout expired while running the script."
    except FileNotFoundError:
        return None, "Python interpreter not found."
    
def find_compile_errors(directory, test_cases):
    compile_errors = {}
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            print("%s代码执行中"%filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            for i, (input_data, _) in enumerate(test_cases, 1):
                stdout, stderr = run_python_code(code,input_data)
                if stderr:
                    # stderr = stderr.split('\n')[-1]
                    compile_errors[filename] = f"{stderr}"
                    break
    return compile_errors

def save_errors_to_json(errors_dict, output_file):
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(errors_dict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    xml_file = "D:\\CQU\\项目\\python机器人数据\\testcase\\testcase_3029.xml"
    code_path = "D:\\CQU\\项目\python机器人数据\\prombleCode\\3029"
    error_path = "D:\\CQU\\项目\\python机器人数据\\prombleCode\\error.json"
    test_cases = parse_test_cases(xml_file)
    compile_errors = find_compile_errors(code_path, test_cases)
    save_errors_to_json(compile_errors, error_path)
