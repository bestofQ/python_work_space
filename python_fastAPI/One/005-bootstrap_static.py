'''
Author: 凃建强
Date: 2020-08-09 19:23:21
LastEditTime: 2020-08-09 19:51:11
Description: FastAPI应用bootstrap
FilePath: \python_work_space\python_work_space\python_fastAPI\One\005-bootstrap_static.py
'''
from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
# 模板
templates = Jinja2Templates(directory='templates')
# 静态文件
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.post('/user/')
async def files(
                    request: Request,
                    username: str = Form(...),
                    password: str = Form(...),
                ):
    print('username', username)
    print('password', password)
    return templates.TemplateResponse(
        '005_index.html',
        {
            'request': request,
            'username': username,
        })

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('005_sigin.html', {'request': request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)