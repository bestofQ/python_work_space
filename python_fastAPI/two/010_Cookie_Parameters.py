'''
Author: 凃建强
Date: 2020-08-24 20:54:30
LastEditTime: 2020-08-24 20:58:06
Description: cookie的使用
FilePath: \python_work_space\python_work_space\python_fastAPI\two\010_Cookie_Parameters.py
'''
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get('/items')
async def read_item(*, ads_id: str = Cookie(None)):
    return {'ads_id': ads_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)