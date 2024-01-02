# from fastapi import FastAPI
from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory='templates/')

router = APIRouter()

@router.get("/")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="homes\welcomes.py"
                                      , context={"request":request})

@router.get("/", response_class=HTMLResponse)
# @app.get("/home") 
async def home():
    html = "<body> <h2>It is home.</h2> </body>"
    return html

@router.get("/list", response_class=HTMLResponse)
# @app.get("/home/list") # 어노테이션 (웹에서 업무(function 호출))
async def home_list():
    # pass
    # return 0
    html = "<body> <h2>It is home list.</h2> </body>"
    return html