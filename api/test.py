from typing import Optional
import os

from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pyperclip

from src.file_process import OpenFileProcess, SaveFileProcess
from config import EXAMPLE_FILES_PATH, CACHE_DIR, WORKING_PATH

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("choose_file.html", {"request": request})


def process_file(file_path, open_scenario, use_custom_lib=False, key=None):
    f_process = OpenFileProcess(file_path, use_custom_lib=use_custom_lib, open_scenario=open_scenario, key=key)
    expressions = f_process.decode()

    message = ""
    expressions_data = {"Expressions": {}}
    for ex in expressions:
        try:
            ex.calculate()
            description = ex.get_description()
            message += description + "\n\n"
            ex_dict_data = ex.get_dict()
            for key, data in ex_dict_data.items():
                expressions_data["Expressions"][key] = data
        except Exception as e:
            error = "Error: {e}"
    return message, expressions_data


@app.post("/download/")
async def upload_file(
    file_option: str = Form(...),
    file_name: str = Form(...),
    file_format: str = Form(...),
    use_custom_libs: bool = Form(...),
    expressions_data: str = Form(...)
):
    print(expressions_data)
    return "help"


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), file_option: str = Form(...), key: Optional[str] = Form(None),
                      use_custom_libs: bool = Form(...)):
    file_path = os.path.join(CACHE_DIR, file.filename)

    with open(file_path, "wb") as file_object:
        file_object.write(file.file.read())

    message, expressions_data = process_file(file_path, file_option, use_custom_libs, key)

    return {"message": message, "expressions_data": expressions_data}
