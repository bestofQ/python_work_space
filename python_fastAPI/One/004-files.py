'''
Author:凃建强
Date: 2020-08-08 22:17:25
LastEditTime: 2020-08-08 22:31:51
Description: 文件上传&展示
FilePath: \python_work_space\python_work_space\python_fastAPI\One\004-files.py
'''
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('004_post.html', {'request': request})

@app.post("/files/")
async def files(
                    request: Request,
                    files_list: List[bytes]         = File(...),
                    files_name: List[UploadFile]    = File(...),
                ):
    return templates.TemplateResponse("004_index.html",
            {
                "request":      request,
                "file_sizes":   [len(file) for file in files_list],
                "filenames":    [file.filename for file in files_name],
             })


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)