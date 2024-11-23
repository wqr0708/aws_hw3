import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "Qianran Wu"}

@app.get("/uni/{uni_id}")
def read_item(uni_id: str, q: Union[str, None] = None):
    return {"uni_id": uni_id, "q": q}