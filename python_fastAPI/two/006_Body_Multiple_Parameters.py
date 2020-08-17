'''
Author: 凃建强
Date: 2020-08-17 23:05:19
LastEditTime: 2020-08-17 23:35:00
Description: 主体--多个参数 -- 嵌套 body
FilePath: \python_work_space\python_work_space\python_fastAPI\two\006_Body_Multiple_Parameters.py
'''

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

# 混合参数
@app.put('/items1/{item_id}')
async def update_item1(
    *,
    item_id: int = Path(..., title='The ID of the item to get', ge=0, le=1000),
    q: str = None,
    item: Item = None,
):
    result = {'item_id': item_id}
    if q:
        result.update({'q': q})
    if item:
        result.update({'item': item})
    return result

# 匿名body
@app.put('items2/{/item_id}')
async def update_item2(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(...)
):
    results = {'item_id': item_id, 'item': item, 'user': user,
    'importance': importance}
    return results

# 嵌入单个body参数
@app.put('/items3/{item_id}')
async def update_item3(
    *,
    item_id: int,
    item: Item = Body(..., embed=True) # embed=True嵌入 --> 相当于 key：vaule
):
    results = {'item_id': item_id, 'item': item}
    return results

# 多主体参数和查询
@app.put("/items4/{item_id}")
async def update_item4(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: str = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({'q': q})
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)