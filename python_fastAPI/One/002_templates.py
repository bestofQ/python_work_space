'''
Author: 凃建强
Date: 2020-08-06 23:02:13
LastEditTime: 2020-08-07 21:37:44
LastEditors: Please set LastEditors
Description: FastAPI-jinja2的模板渲染
FilePath: \python_work_space\python_work_space\python_fastAPI\One\002_templates.py
'''
from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
# pip jinja2 、 aiofiles
app = FastAPI()
# templates用于存放模板
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    # 传参、类型
    # index.html --> templates文件夹中的html
    # hello --> 代表键，用于 html中的 传值
    return templates.TemplateResponse('002_index.html', {'request': request, 'hello': 'HI...'})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
