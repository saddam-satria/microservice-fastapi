from fastapi import FastAPI
from routes import productRoute
from database import engine
import uvicorn


app = FastAPI(docs_url="/doc")
app.include_router(productRoute)

@app.on_event("startup")
def startUP():
    engine.connect()

@app.on_event("shutdown")
def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)