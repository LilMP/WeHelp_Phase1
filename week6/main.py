from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
# from pydantic import BaseModel
from fastapi import Body
import mysql.connector


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
    return templates.TemplateResponse(name = "home.html", context = {"request": request, "title": "歡迎光臨，請註冊登入系統", "signup":"註冊帳號","signin": "登入系統", "bonus":"計算正整數的平方"})

@app.post('/signup')
async def signup(request: Request, new_name: str = Form("new_name"), new_account: str = Form("new_account"), new_password: str = Form("new_password")):
    # username = request.session.get('ACCOUNT')
    mydb = mysql.connector.connect(
        host='localhost',
        user='wehelp',
        password='test123',
        database='website'
    )
    # print(mydb)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM member WHERE username = %s;"
    val = (new_account,)
    mycursor.execute(sql, val)
    msg = mycursor.fetchone()  
    
    if msg is None: # 資料庫中沒重複帳號名稱
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (new_name, new_account, new_password)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return RedirectResponse("/",status_code=303)
    else:
        return RedirectResponse(
            url = "/error"+ "?message=此帳號已被註冊", # URL query string
            status_code=303
        )   
   
@app.get('/member')
def get_member(request: Request):
    username = request.session.get('NAME')

    # check session SIGNED-IN
    if request.session.get("SIGNED-IN") is True:

        # fetch all messages from database
        mydb = mysql.connector.connect(
            host='localhost',
            user='wehelp',
            password='test123',
            database='website'
        )
        
        mycursor = mydb.cursor()
        sql = "SELECT member.name AS sender_name, message.content, message.time FROM member INNER JOIN message ON member.id =  message.member_id  ORDER BY message.time DESC;"
        mycursor.execute(sql)
        msg = mycursor.fetchall()  
        
        messages = []
        row_count = 0
        for item in msg:
            if(username!=item[0]):
                messages.append({"name":item[0],"message":item[1],"delete":"none"})
            else:
                messages.append({"name":item[0],"message":item[1],"delete":"inline-block"})
            row_count+=1



        
        return templates.TemplateResponse("member.html", {"request": request, "title": "歡迎光臨，這是會員頁", "username": username, "messages": messages})
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
    request.session.update({"MEMBER-ID":None})
    request.session.update({"USERNAME":None})
    request.session.update({"NAME":None})

    return RedirectResponse('/')  

@app.post('/signin')
async def verification(request: Request, account: str = Form("account"), password: str = Form("password")):
    # print(password)
    # print(account)
    mydb = mysql.connector.connect(
        host='localhost',
        user='wehelp',
        password='test123',
        database='website'
    )
    mycursor = mydb.cursor()
    sql = "SELECT id, username, password, name FROM member WHERE username = %s;"
    val = (account,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()  
    
    if myresult is None: # 輸入不存在資料庫裡的帳號
        request.session.update({"SIGNED-IN": False})
        return RedirectResponse(
            url = "/error"+ "?message=帳號不存在", # URL query string
            status_code=303
        )
    db_id = myresult[0]
    db_account = myresult[1]
    db_password = myresult[2]
    db_name = myresult[3]
    

    # check submitted inputs with default account/password
    if account == db_account and password == db_password:
        request.session.update({"SIGNED-IN": True})
        request.session.update({"MEMBER-ID": db_id})
        request.session.update({"USERNAME": db_account})
        request.session.update({"NAME": db_name})

        return RedirectResponse('/member', status_code=303)  
        # update cookie 的寫法
        # response = RedirectResponse('/member', status_code=303)
        # response.set_cookie(key="account", value=account)
        # return response 
    elif account == db_account and password != db_password:
        request.session.update({"SIGNED-IN": False})
        return RedirectResponse(
            url = "/error"+ "?message=密碼輸入錯誤", # URL query string
            status_code=303
        )
        



@app.post('/createMessage')
async def create_message(request: Request, comment: str = Form("comment")):

    id = request.session.get('MEMBER-ID')
    # username = request.session.get('USERNAME')
    
    # fetch all messages from database
    mydb = mysql.connector.connect(
        host='localhost',
        user='wehelp',
        password='test123',
        database='website'
    )
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s);"
    val = (id, comment)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "message inserted.")
    # msg = mycursor.fetchall()  


    return RedirectResponse('/member', status_code=303)  

# class Item(BaseModel):
#     name: str
#     message: str

@app.post('/deleteMessage')
async def delete_message(request: Request, message: str = Form("message"), name: str = Form("name") ):
# async def delete_message(request: Request, item: Item ):
# def delete_message(request: Request, message = Body("message"), name = Body("name") ):    
    print(message)
    print(name)
    # print(item.message)
    # print(item.name)
    # cookie_id = request.session.get('MEMBER-ID')
    cookie_name = request.session.get('NAME')
    # print(cookie_id)
    print(cookie_name)

    # deletion happens only when cookie_name equals to the name passed from front-end
    if(cookie_name != name):
        print("someone is doing bad thing...not okay")
        print("redirect to member page")
    else:
        mydb = mysql.connector.connect(
            host='localhost',
            user='wehelp',
            password='test123',
            database='website'
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM message WHERE content = %s"
        msg = (message, ) # 必須是list,tuple,dict型態!
        mycursor.execute(sql, msg)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

    return RedirectResponse('/member', status_code=303)  


#讓terminal 可以執行 python main.py
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run("main:app", reload=True)