from fastapi import FastAPI
from route import routing
from database import engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(docs_url="/doc")
routing(app)

origins = ["*"]

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


@app.on_event("startup")
def startUP():
    engine.connect()

@app.on_event("shutdown")
def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)