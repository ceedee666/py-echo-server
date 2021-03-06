import uvicorn
import socket

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root(request: Request):
    return {
            "client": request.client.host,
            "host": socket.gethostname(),
            "message": "Hello World from Python!"
            }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
