from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware


middleware = [
    Middleware(SessionMiddleware, secret_key = ...)
]

app = FastAPI(middleware=middleware)


app.mount("/static", StaticFiles(directory="static"), name="static") # 載入css檔案
templates = Jinja2Templates(directory="templates")  # 把要當作模板的網頁存到templates資料夾

class User:
    def __init__(self,account,password):
        self.account = account
        self.password = password

default_user = User("test", "test")
# 模擬database裡的資料
database = {
    0: default_user
}


@app.get('/')
async def home_page(request: Request):
    return templates.TemplateResponse(name = "home.html", context = {"request": request, "title": "歡迎光臨，請輸入帳號密碼", "status": "登入系統", "bonus":"計算正整數的平方"})

@app.get('/member')
def get_member(request: Request):
    account = request.session.get('ACCOUNT')
    # print(account)
    # check session SIGNED-IN
    if request.session.get("SIGNED-IN") is True:
        return templates.TemplateResponse("member.html", {"request": request, "title": "歡迎光臨"+account+"，這是會員頁", "status": "恭喜您，成功登入系統"})
    else:
        return RedirectResponse('/')   

@app.get('/error')
def get_error(request: Request, message):
    request.session.update({"SIGNED-IN":False})
    return templates.TemplateResponse("error.html", {"request":request, "title":"失敗頁面", "status":message})

@app.get('/signout')
def get_signout(request: Request):
    # set signed-in state to false, then redirect to /
    request.session.update({"SIGNED-IN":False})
    return RedirectResponse('/')  

@app.post('/signin')
def verification(request: Request, account: str = Form("account"), password: str = Form("password")):

    # check submitted nputs with default account/password
    if account == database[0].account and password == database[0].password:
        request.session.update({"SIGNED-IN": True})
        request.session.update({"ACCOUNT": account})
        return RedirectResponse('/member', status_code=303)  
        # update cookie 的寫法
        # response = RedirectResponse('/member', status_code=303)
        # response.set_cookie(key="account", value=account)
        # return response 
    elif account == "test" and password != "test":
        request.session.update({"SIGNED-IN": False})
        return RedirectResponse(
            url = "/error"+ "?message=密碼輸入錯誤", # URL query string
            status_code=303
        )
    else:
        request.session.update({"SIGNED-IN": False})
        return RedirectResponse(
            url = "/error"+ "?message=帳號不存在", # URL query string
            status_code=303
        )

# bonus
@app.get('/square/{int_input}')
def cal_square(request:Request, int_input: int):
    # print("print input")
    # print(type(int_input))
    return templates.TemplateResponse("error.html", { "request":request, "title":"正整數平方計算結果", "status":str(int_input)+"^2="+str(int_input**2)})


