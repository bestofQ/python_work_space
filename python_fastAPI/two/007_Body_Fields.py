'''
Author: 凃建强
Date: 2020-08-18 22:33:04
LastEditTime: 2020-08-18 22:48:48
Description: 字段验证
FilePath: \python_work_space\python_work_space\python_fastAPI\two\007_Body_Fields.py
'''
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = Field(None, title="The description of the item", max_length=6)  # 最大6位
    price: float     = Field(..., gt=0, description="The price must be greater than zero") # 大于0 需要验证
    tax: float       = None

class Zzz(BaseModel):
    name: str
    description: str = None
    price: float     = Field(..., gt=0)
    tax: float       = None

@app.put('/items1/{item_id}')
async def update_item1(
    *,
    item_id: int,
    item: Item = Body(..., embed=True)
):
    results = {'item_id': item_id, 'item': item}
    return results

@app.put('/items2/{item_id}')
async def update_item2(
    *,
    item_id: int,
    zzz: Zzz = Body(
        ...,
        example = {# example是Body里没有的字段；不会添加任何验证，而只会添加注释；不是example也不行
        # 而且数量必须和Zzz的一致
            "name": "Foo",
            "description": "A very nice Item",
            "price": 0,
            "toooo": 3.2,
            # "toooooooooo": 3.2, # 超过的键值对，会全部显示原来的Item
        }
    )
):
    results = {"item_id": item_id, "zzz": zzz}
    return results



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)