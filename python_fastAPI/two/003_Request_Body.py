'''
Author: 凃建强
Date: 2020-08-13 22:46:52
LastEditTime: 2020-08-13 23:02:22
Description: pydantic创建一个requestbody，方便使用
FilePath: \python_work_space\python_work_space\python_fastAPI\two\003_Request_Body.py
'''
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import main

# 创建一个 基于BaseModel的类 ---> 字典类型
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.post('/items')
async def create_item(item: Item):
    print(item.dict())
    return item, '人生苦短，我学python'

@app.put('/items/{item_id}')
async def create_item2(item_id: int, item: Item, q: str = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    print(result)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)