'''
Author: 凃建强
Date: 2020-08-05 21:55:46
LastEditTime: 2020-08-05 22:50:08
Description: FastAPI学习第一讲-helloworld
FilePath: \python_work_space\python_work_space\python_fastAPI\第一季\001-helloword.py
'''
# 安装两个第三方库 fastapi\uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello，FastAPI"}


if __name__ == '__main__':
    # app -- app的name
    # host -- localhost的ip地址
    # port -- 端口
    # 等价于
    # uvicorn 001_helloworld.py:app --reload
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)