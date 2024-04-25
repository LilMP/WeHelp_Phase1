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
    
    # print("homepage: 印出request.session:")
    # print(request.session.get("SIGNED-IN"))

    
    # request.session.update({"session_cookie":{"signed":False}})
    # print(request.session.get("session_cookie"))
    # print(request.headers)
    # return templates.TemplateResponse("home.html", {"request": request, "title": "歡迎光臨，請輸入帳號密碼", "status": "登入系統"})
    return templates.TemplateResponse(name = "home.html", context = {"request": request, "title": "歡迎光臨，請輸入帳號密碼", "status": "登入系統", "bonus":"計算正整數的平方"})

@app.get('/member')
def get_member(request: Request):
    # request.session.update({"SIGNED-IN": False})
    # check session SIGNED-IN
    print("member: check request.session")
    print(request.session.get("SIGNED-IN"))
    if request.session.get("SIGNED-IN") is True:
        return templates.TemplateResponse("member.html", {"request": request, "title": "歡迎光臨，這是會員頁", "status": "恭喜您，成功登入系統"})
    else:
        return RedirectResponse('/',status_code=303)   


@app.get('/error')
def get_error(request: Request, message):
    print("error:印出request.session")
    print(request.session.get("SIGNED-IN"))
    return templates.TemplateResponse("error.html", { "request":request, "title":"失敗頁面", "status":message})

@app.get('/signout')
def get_signout(request: Request):
    # set signed-in state to false
    print("signout:印出request.session")
    print(request.session.get("SIGNED-IN"))
    request.session.update({"SIGNED-IN":False})
    return RedirectResponse('/',status_code=303)  
    # return templates.TemplateResponse("signout.html", {"request":request, "title":"失敗頁面", "status":"帳號、或密碼輸入錯誤"})

@app.post('/signin')
def verification(request: Request, account: str = Form("account"), password: str = Form("password")):
    # print("帳號: ",account)
    # print("密碼: ",password)
    print("verification:印出request.session")
    print(request.session.get("SIGNED-IN"))

    if account == database[0].account and password == database[0].password:
        request.session.update({"SIGNED-IN": True})
        # redirect_url = request.url_for('member') 
        return RedirectResponse('/member',status_code=303)   
    elif account == "test" and password != "test":
        request.session.update({"SIGNED-IN": False})
        return RedirectResponse(
            url = "/error"+ "?message=密碼輸入錯誤",
            status_code=303
        )
    else:
        request.session.update({"SIGNED-IN": False})
        # redirect_url = request.url_for('error') 
        # return RedirectResponse('/error',status_code=303) 
        return RedirectResponse(
            url = "/error"+ "?message=帳號不存在",
            status_code=303
        )
        
@app.get('/square/{int_input}')
def cal_square(request:Request, int_input: int):
    print("print input")
    print(type(int_input))
    
    return templates.TemplateResponse("error.html", { "request":request, "title":"正整數平方計算結果", "status":int_input**2})


