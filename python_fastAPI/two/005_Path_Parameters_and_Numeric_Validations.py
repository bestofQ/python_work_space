'''
Author: 凃建强
Date: 2020-08-15 19:05:40
LastEditTime: 2020-08-15 19:45:17
LastEditors: Please set LastEditors
Description: 路劲参数和数值验证
FilePath: \python_work_space\python_work_space\python_fastAPI\two\005_Query_Parameters_and_String_Validations.py
'''

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(
    item_id: int = Path(...,
                        title = 'The ID Of The Item To Get',
                        ge = 50,  # ge 大于等于  le是小于等于
                        le = 100  # le是小于等于
                        ),
    q: str       = Query(None,
                         alias='item-query'),
    size: float  = Query(1,
                         gt=0,  # gt是大于
                         lt=10.5) # lt小于
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000 )