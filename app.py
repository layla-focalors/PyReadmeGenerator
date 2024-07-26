import json

PATH = "./base/"

def Markdown_Read(path):
    with open(path, 'r') as file:
        return file.read()

def Json_Read(path):
    with open(path, 'r') as file:
        return json.load(file)
    
def CreateComponentJob():
    data = Json_Read('./base/job.json')
    export = []
    for i in data:
        export.append(f'{i["date"]} | {i["task"]}')
        
    return export
print(CreateComponentJob())
