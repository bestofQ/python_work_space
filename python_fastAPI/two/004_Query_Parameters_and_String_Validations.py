'''
Author: 凃建强
Date: 2020-08-15 01:31:33
LastEditTime: 2020-08-15 02:03:10
Description: 查询
FilePath: \python_work_space\python_work_space\python_fastAPI\two\004_Query_Parameters_and_String_Validations.py
'''
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# 限制长度
@app.get('/items/')
async def read_items(
        q: str = Query(
                None,  # 默认值
                min_length=3,  # 最小3
                max_length=50  # 最大50
    )):
    #填None就是默认值   填 ...则是必填项
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get('/items2/')
async def read_items2(q: str = Query(None, min_length=3, max_length=50, regex='^nice')):
    # 正则表达式：传值必须 nice 开头
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#列表
@app.get("/items3/")
async def read_items3(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items

#别名参数
@app.get("/items4/")
async def read_items4(q: str = Query(None, alias="item-query")):
    # alias 设置别名。传参赋值的时候，必须使用别名进行对接
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#弃用参数  ？？？？？暂时不明白 2020.08.15提出
@app.get("/items5/")
async def read_items5(
    q: str = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)