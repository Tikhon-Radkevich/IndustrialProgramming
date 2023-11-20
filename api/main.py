import logging
from logging.config import fileConfig

from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import CACHE_DIR


fileConfig("logging.ini")
logger = logging.getLogger(__name__)
import toplevel


app = FastAPI()
templates = Jinja2Templates(directory="api/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    with open(f"{CACHE_DIR}/{file.filename}", "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}
