from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/",response_class=HTMLResponse)
async def get(requests:Request):
    return templates.TemplateResponse("chat.html",{"request":requests})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")