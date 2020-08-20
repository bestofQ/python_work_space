'''
Author: 凃建强
Date: 2020-08-20 20:28:46
LastEditTime: 2020-08-20 20:45:03
LastEditors: Please set LastEditors
Description: body -- 嵌入式
FilePath: \python_work_space\python_work_space\python_fastAPI\two\008_Body_Nested_Models.py
'''
from typing import List, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str                       # string
    description: str  = None        # string
    price: float                    # 0
    tax: float        = None        # 0
    tags0: list       = []          # [null]
    tags1: List[str]  = []          # [string]
    tags2: Set[str]   = set()       # [string]

class Image(BaseModel):
    url: str
    name: str

class Item1(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set()  # 集合 创建一个空集合必须用 set() 而不是 { }
    image: Image = None # 使用子模型作为类型
    images: List[Image] = None # 带有子模型列表的属性

@app.put("/items1/{item_id}")
async def update_item1(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# 到处都有编辑器支持
@app.put("/items2/{item_id}")
async def update_item2(*, item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results

# url
class Image(BaseModel):
    url: HttpUrl    # 该字符串将被检查为有效的URL，并在JSON Schema / OpenAPI中进行记录。
                    # 特殊类型和验证 https://pydantic-docs.helpmanual.io/usage/types/
    name: str

# 纯列表体
# @app.post("/images/multiple/")
# async def create_multiple_images(*, images: List[Image]):
#     return images

# # 任意dicts (无需事先知道有效的字段/属性名称是什么)(如果您想接收未知的密钥，这将很有用。)
# @app.post("/index-weights/")
# async def create_index_weights(weights: Dict[int, float]):
#     return weights

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)