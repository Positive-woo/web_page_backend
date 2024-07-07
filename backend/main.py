# main.py
from fastapi import FastAPI

import uvicorn

from backend.apis.post import post_router

app = FastAPI()

app.include_router(post_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
