from fastapi import FastAPI
from .routers import variables

app = FastAPI(title="WMS Variables Service")

app.include_router(variables.router)

@app.get("/")
def root():
    return {"message": "Hello from wms-variables-service!"}