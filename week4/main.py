from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")  # 把要當作模板的網頁存到templates資料夾

class User(BaseModel):
    account: str
    password: str


@app.get('/')
async def title(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "歡迎光臨，請輸入帳號密碼", "status": "登入系統"})

@app.get('/member')
def get_member(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "歡迎光臨，這是會員頁", "status": "恭喜您成功登入系統"})

err_message = "自訂的錯誤訊息"
@app.get('/error')
def get_error(request: Request):
    
    return templates.TemplateResponse("home.html", { "request":request, "title":"失敗頁面", "status":"帳號、或密碼輸入錯誤"})

# @app.get('signout')

@app.get('/signin')
def verification(request: Request):

    return templates.TemplateResponse("home.html", {"request": request, "title": "歡迎光臨，這是會員頁", "status": "恭喜您成功登入系統"})
