'''
Author: 凃建强
Date: 2020-08-07 21:38:01
LastEditTime: 2020-08-07 23:57:59
Description: FastAPI--form
FilePath: \python_work_space\python_work_space\python_fastAPI\One\003_form_post.py
'''
from starlette.requests import Request
from fastapi import FastAPI, Form
# 如果要使用request.form（）支持表单“解析”，则为必需 python-multipart
# pip install python-multipart
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.post("/user/") # 接受post请求
async def form_text(request: Request,
                     username: str = Form(...), # 直接去请求体里面获取username键对应的值并自动转化成字符串类型
                     password: str = Form(...) # 直接去请求体里面获取password键对应的值并自动转化成整型
                     ):
    print('username', username)
    print('password', password)
    return templates.TemplateResponse('003_index.html', {
                        'request': request,
                        'username': username,
                        'password': password
                })

@app.get("/")
async def main(request: Request):
    print('main')
    return templates.TemplateResponse('003_post.html', {'request': request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

