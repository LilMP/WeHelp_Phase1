from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
# from typing import Union
from pydantic import BaseModel

app = FastAPI()

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    main block
</body>
</html>
"""



@app.get("/")
async def index():
    # return HTMLResponse(content=html)
    return FileResponse("index.html")

@app.get("/main.css")
async def css():
    return FileResponse("main.css")

# @app.get("/signin")
# async def signin():
#     print("in signin page")

@app.post("/signin")
def read_item(account: str = Form("account"), password: str = Form("password")):
    if(0):
        return FileResponse("success.html")
    else:
        return FileResponse("error.html")

    # return {"account": account, "password": password}