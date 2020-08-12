'''
Author: 凃建强
Date: 2020-08-12 22:38:32
LastEditTime: 2020-08-12 23:13:15
LastEditors: Please set LastEditors
Description: 获取查询参数
FilePath: \python_work_space\python_work_space\python_fastAPI\two\002_Query_Parameters_1.py
'''
from fastapi import FastAPI

app = FastAPI()
# 创建一个列表
fake_item_db = [
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'}
]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    # skip默认 0 ， limit 默认 10
    # 如果没有查询参数传入，使用默认值
    return fake_item_db[skip: skip + limit]

@app.get('/i/')
async def i(A: str = 'HI...', B: str = 'Hello...', C: str = 'He...'):
    return {'cc': A+B+C},{'dd': B+C}

# 多路径 、 查询参数 、 必填字段
@app.get('/user/{user_id}/item/{item_id}')
async def read_user_item(
            user_id: int,   # int类型，没有默认值，必须输入
            item_id: str,   # str类型，没有默认值，必须输入
            q: str = None,  # str类型，有默认值，输入的值会覆盖默认值
            short: bool = False     # bool类型，有默认值，输入的值会覆盖默认值
):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        # 类似于 list.append()
        item.update({'q': q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
