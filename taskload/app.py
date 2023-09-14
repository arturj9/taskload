from fastapi import FastAPI

from taskload.routes import tasks

app = FastAPI(title='TaskLoad')

app.include_router(tasks.router)


@app.get('/')
def read_root():
    return {'message': 'taskload is running...'}
