'''
Author: 凃建强
Date: 2020-08-11 22:54:16
LastEditTime: 2020-08-11 23:07:07
Description: 进阶版：枚举法
FilePath: \python_work_space\python_work_space\python_fastAPI\two\001_url_2.py
'''
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# 枚举
class Name(str, Enum):
    A = 'Ali'
    B = 'bobo'
    C = 'cc'

@app.get('/{who}')
async def get_name(who: Name):
    # 类型 枚举类 Name --> .value = 赋值 ？
    if who == Name.A:
        return {"who": who, "message": "Ali是中国人"}
    if who.value == 'bobo':
        return {"who": who, "message": "bobo是美国人"}
    return {"who": who, "message": "cc是英国人"}

@app.get('/')
async def main():
    return {"message": "001进阶：枚举大法"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
