from typing import Optional
import json
import os

from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
# import pyperclip

from src.file_process import OpenFileProcess, SaveFileProcess
from config import CONTENT_TYPES, CACHE_DIR, WORKING_PATH

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")
app.mount("/static", StaticFiles(directory="api/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
            error = f"Error: {e}"
    return message, expressions_data


# @app.post("/download/")
# async def upload_file(
#         file_option: str = Form(...),
#         file_name: str = Form(...),
#         file_extension: str = Form(...),
#         use_custom_libs: bool = Form(...),
#         expressions_data: str = Form(...)
# ):
#     data = json.loads(expressions_data)
#     file_content = json.dumps(data)
#     file_name_with_extension = f"{file_name}{file_extension}"
#     file_path = f"{CACHE_DIR}/{file_name_with_extension}"
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(file_content)
#
#     content_type = CONTENT_TYPES.get(file_extension)
#
#     return FileResponse(
#         path=file_path,
#         filename=file_name_with_extension,
#         media_type=content_type
#     )

@app.post("/download/")
async def upload_file(
        file_option: str = Form(...),
        file_name: str = Form(...),
        file_extension: str = Form(...),
        use_custom_libs: bool = Form(...),
        expressions_data: str = Form(...)
):
    data = json.loads(expressions_data)
    file_content = json.dumps(data)
    file_name_with_extension = f"{file_name}{file_extension}"
    file_path = f"{CACHE_DIR}/{file_name_with_extension}"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    f_process = OpenFileProcess(file_path)
    expressions = f_process.decode()

    expressions_data = {"Expressions": {}}

    for ex in expressions:
        ex.calculate()
        ex_dict_data = ex.get_dict()
        for key, data in ex_dict_data.items():
            expressions_data["Expressions"][key] = data

    f_process = SaveFileProcess(file_option, file_path, file_extension, use_custom_libs)
    key = f_process.save(expressions_data, False)

    if "zip" in file_option:
        file_path = "/".join(file_path.split("/")[:-1]) + f"/{file_name}.zip"
        file_name_with_extension = file_name + ".zip"

    return FileResponse(
        path=file_path,
        filename=file_name_with_extension,
    )


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), file_option: str = Form(...), key: Optional[str] = Form(None),
                      use_custom_libs: bool = Form(...)):
    file_path = os.path.join(CACHE_DIR, file.filename)

    with open(file_path, "wb") as file_object:
        file_object.write(file.file.read())

    message, expressions_data = process_file(file_path, file_option, use_custom_libs, key)

    return {"message": message, "expressions_data": expressions_data}
