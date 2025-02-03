from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from enum import Enum
from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
from enum import Enum

class schemas1(BaseModel):
    name:str
    section:str
    roll_no:int
    
class choiceName(str, Enum):
    one = "first"
    two = "second"
    third = "third"

app = FastAPI()

@app.get("/hello")
async def root():
    return("message","hello world")

@app.get("/{Item}")
def path_fun(Item):
    var_name = {"path variables":  Item}
    return (var_name)

@app.get("/query/")
def query_fun(name:Union[str,None]=None,roll_no:Union[str, None]= Query(default = None,min_length=2,max_length=3)):
    var_name = {"name":name,"roll_no":roll_no}
    return (var_name)

@app.get("/models/{model_name}")
async def get_model(model_name: choiceName):
    if model_name.value == "first" :
        return {"model_name": model_name, "message": "calling first!"}

    if model_name.value == "second":
        return {"model_name": model_name, "message": "calling second"}

    return {"model_name": model_name, "message": "calling third"}

#request body
@app.post("/items/")
async def create_item(item: schemas1):
    return item

#form data
@app.post("/form/data")
def form_data(username : str = Form(),password:int = Form()):
    return ("username", username,"password",password)

#file upload
@app.post("/file/upload")
def files_bytes(file:bytes = File()):
    return ("File",len(file))

@app.post("/upload/file")
def files_upload(file : UploadFile):
    return ({"File_name":file.filename,"file_content_name":file.content_type})

#combining all 3 (form,file,uploading)
@app.post("/form/data/filedata")
def form_dataupload(file1:UploadFile, file2:bytes = File(), name:str = Form()):
    return({"file_name":file1.filename,"file2_bytes":len(file2),"name": name})
