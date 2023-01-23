from fastapi import FastAPI
from route import routing
from database import engine
import uvicorn


app = FastAPI(docs_url="/doc")
routing(app)


@app.on_event("startup")
def startUP():
    engine.connect()

@app.on_event("shutdown")
def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)