'''
Author: 凃建强
Date: 2020-08-11 22:37:09
LastEditTime: 2020-08-11 22:53:36
Description: url和交互式API文档
FilePath: \python_work_space\python_work_space\python_fastAPI\two\001_url.py
'''

from fastapi import FastAPI

app = FastAPI()
# /me/xx  --> 等价于 127.0.0.1:8000/me/xx
# 如果url的路径一致，网页获取的信息，以第一个为主
@app.get('/me/xx')
async def read_item_me():
    return {"me": 'me'}

@app.get('/me/{item_id}')
async def read_item(item_id: str):
    # 这里 定义了 item_id的类型为str
    # 如果传参为int类型，会报错。20200811尝试，没有报错，可能是最近更新过了
    return {"item_id", item_id}

@app.get('/')
async def main():
    return {"message":" Hello, FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)