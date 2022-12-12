from fastapi import APIRouter
from fastapi import FastAPI, status, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

from pathlib import Path


#########################################################
# CREATE AN INSTANCE OF FASTAPI CLASS
#########################################################
app = FastAPI()


#########################################################
# TEMPLATES
#########################################################
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


#########################################################
# STATIC FILES
#########################################################
import os
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")


#########################################################
# GET - NAVIOS CADASTRADOS
#########################################################
@app.get("/navios_cadastrados/", response_class=HTMLResponse)
async def get_navios_cadastrados(
    request: Request,
    ):
    navios = usersEntity(conn.local.user.find())
    return templates.TemplateResponse("navios_cadastrados.html", {"request": request, "navios": navios})


# @app.get('/')
# async def find_all_users():
#     print(conn.local.user.find())
#     print(usersEntity(conn.local.user.find()))
#     return usersEntity(conn.local.user.find())


# @app.post('/')
# async def create_user(user: User):
#     conn.local.user.insert_one(dict(user))
#     return usersEntity(conn.local.user.find())


#########################################################
# GET - CADASTRAR NAVIO
#########################################################
@app.get("/cadastrar_navio/", response_class=HTMLResponse)
async def get_cadastrar_navio(
    request: Request,
    ):
    return templates.TemplateResponse("cadastrar_navio.html", {"request": request})


#########################################################
# POST - CADASTRAR NAVIO
#########################################################
@app.post('/cadastrar_navio/')
async def post_cadastrar(
    navio_parametro_01: str = Form(...),
    navio_parametro_02: float = Form(...),
    navio_parametro_03: float = Form(...),
    navio_parametro_04: float = Form(...),
    navio_parametro_05: float = Form(...),
    navio_parametro_06: float = Form(...),
    navio_parametro_07: float = Form(...),
    navio_parametro_08: float = Form(...),
    navio_parametro_09: float = Form(...),
    navio_parametro_10: float = Form(...),
    navio_parametro_11: float = Form(...),
    navio_parametro_12: float = Form(...),
    navio_parametro_13: float = Form(...),
    navio_parametro_14: float = Form(...),
    navio_parametro_15: float = Form(...),
    navio_parametro_16: float = Form(...),
    navio_parametro_17: float = Form(...),
    navio_parametro_18: float = Form(...),
    navio_parametro_19: float = Form(...),
    navio_parametro_20: float = Form(...),
    navio_parametro_21: float = Form(...),
    navio_parametro_22: float = Form(...),
    navio_parametro_23: float = Form(...),
    navio_parametro_24: float = Form(...),
    navio_parametro_25: float = Form(...)
    ):

    # montango o json (a partir dos dados recebidos do formulario)

    navio = {
        "navio_parametro_01": navio_parametro_01,
        "navio_parametro_02": navio_parametro_02,
        "navio_parametro_03": navio_parametro_03,
        "navio_parametro_04": navio_parametro_04,
        "navio_parametro_05": navio_parametro_05,
        "navio_parametro_06": navio_parametro_06,
        "navio_parametro_07": navio_parametro_07,
        "navio_parametro_08": navio_parametro_08,
        "navio_parametro_09": navio_parametro_09,
        "navio_parametro_10": navio_parametro_10,
        "navio_parametro_11": navio_parametro_11,
        "navio_parametro_12": navio_parametro_12,
        "navio_parametro_13": navio_parametro_13,
        "navio_parametro_14": navio_parametro_14,
        "navio_parametro_15": navio_parametro_15,
        "navio_parametro_16": navio_parametro_16,
        "navio_parametro_17": navio_parametro_17,
        "navio_parametro_18": navio_parametro_18,
        "navio_parametro_19": navio_parametro_19,
        "navio_parametro_20": navio_parametro_20,
        "navio_parametro_21": navio_parametro_21,
        "navio_parametro_22": navio_parametro_22,
        "navio_parametro_23": navio_parametro_23,
        "navio_parametro_24": navio_parametro_24,
        "navio_parametro_25": navio_parametro_25
    }

    print(navio)

    # armazenar o json navio na database
    conn.local.user.insert_one(dict(navio))

    # retornar uma pagina html
    # return templates.TemplateResponse("input.html", {"request": request})
    return RedirectResponse("/cadastrar_navio/", status_code=status.HTTP_302_FOUND)