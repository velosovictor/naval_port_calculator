from fastapimport APIRouter
from fastapimport FastAPI, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from pathlib import Path
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity


#########################################################
# CREATE AN INSTANCE OF FASTAPCLASS
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
    coordenadas = usersEntity(conn.local.)
    return templates.TemplateResponse("navios_cadastrados.html", {"request": request, "navios": navios})


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

    coordenadas = {

        "coord_tipo_01": coord_tipo_01,
        "coord_xn_01": coord_xn_01,
        "coord_yn_01": coord_yn_01,
        "coord_zn_01": coord_yn_01,
        "coord_xb_01": coord_yn_01,
        "coord_yb_01": coord_yn_01,
        "coord_zb_01": coord_yn_01,

        "coord_tipo_02": coord_tipo_02,
        "coord_xn_02": coord_xn_02,
        "coord_yn_02": coord_yn_02,
        "coord_zn_02": coord_yn_02,
        "coord_xb_02": coord_yn_02,
        "coord_yb_02": coord_yn_02,
        "coord_zb_02": coord_yn_02,

        "coord_tipo_03": coord_tipo_03,
        "coord_xn_03": coord_xn_03,
        "coord_yn_03": coord_yn_03,
        "coord_zn_03": coord_yn_03,
        "coord_xb_03": coord_yn_03,
        "coord_yb_03": coord_yn_03,
        "coord_zb_03": coord_yn_03,

        "coord_tipo_04": coord_tipo_04,
        "coord_xn_04": coord_xn_04,
        "coord_yn_04": coord_yn_04,
        "coord_zn_04": coord_yn_04,
        "coord_xb_04": coord_yn_04,
        "coord_yb_04": coord_yn_04,
        "coord_zb_04": coord_yn_04,

        "coord_tipo_05": coord_tipo_05,
        "coord_xn_05": coord_xn_05,
        "coord_yn_05": coord_yn_05,
        "coord_zn_05": coord_yn_05,
        "coord_xb_05": coord_yn_05,
        "coord_yb_05": coord_yn_05,
        "coord_zb_05": coord_yn_05,

        "coord_tipo_06": coord_tipo_06,
        "coord_xn_06": coord_xn_06,
        "coord_yn_06": coord_yn_06,
        "coord_zn_06": coord_yn_06,
        "coord_xb_06": coord_yn_06,
        "coord_yb_06": coord_yn_06,
        "coord_zb_06": coord_yn_06,

        "coord_tipo_07": coord_tipo_07,
        "coord_xn_07": coord_xn_07,
        "coord_yn_07": coord_yn_07,
        "coord_zn_07": coord_yn_07,
        "coord_xb_07": coord_yn_07,
        "coord_yb_07": coord_yn_07,
        "coord_zb_07": coord_yn_07,

        "coord_tipo_08": coord_tipo_08,
        "coord_xn_08": coord_xn_08,
        "coord_yn_08": coord_yn_08,
        "coord_zn_08": coord_yn_08,
        "coord_xb_08": coord_yn_08,
        "coord_yb_08": coord_yn_08,
        "coord_zb_08": coord_yn_08,

        "coord_tipo_09": coord_tipo_09,
        "coord_xn_09": coord_xn_09,
        "coord_yn_09": coord_yn_09,
        "coord_zn_09": coord_yn_09,
        "coord_xb_09": coord_yn_09,
        "coord_yb_09": coord_yn_09,
        "coord_zb_09": coord_yn_09,

        "coord_tipo_10": coord_tipo_10,
        "coord_xn_10": coord_xn_10,
        "coord_yn_10": coord_yn_10,
        "coord_zn_10": coord_yn_10,
        "coord_xb_10": coord_yn_10,
        "coord_yb_10": coord_yn_10,
        "coord_zb_10": coord_yn_10,

        "coord_tipo_11": coord_tipo_11,
        "coord_xn_11": coord_xn_11,
        "coord_yn_11": coord_yn_11,
        "coord_zn_11": coord_yn_11,
        "coord_xb_11": coord_yn_11,
        "coord_yb_11": coord_yn_11,
        "coord_zb_11": coord_yn_11,

        "coord_tipo_12": coord_tipo_12,
        "coord_xn_12": coord_xn_12,
        "coord_yn_12": coord_yn_12,
        "coord_zn_12": coord_yn_12,
        "coord_xb_12": coord_yn_12,
        "coord_yb_12": coord_yn_12,
        "coord_zb_12": coord_yn_12,

        "coord_tipo_13": coord_tipo_13,
        "coord_xn_13": coord_xn_13,
        "coord_yn_13": coord_yn_13,
        "coord_zn_13": coord_yn_13,
        "coord_xb_13": coord_yn_13,
        "coord_yb_13": coord_yn_13,
        "coord_zb_13": coord_yn_13,

        "coord_tipo_14": coord_tipo_14,
        "coord_xn_14": coord_xn_14,
        "coord_yn_14": coord_yn_14,
        "coord_zn_14": coord_yn_14,
        "coord_xb_14": coord_yn_14,
        "coord_yb_14": coord_yn_14,
        "coord_zb_14": coord_yn_14,

        "coord_tipo_15": coord_tipo_15,
        "coord_xn_15": coord_xn_15,
        "coord_yn_15": coord_yn_15,
        "coord_zn_15": coord_yn_15,
        "coord_xb_15": coord_yn_15,
        "coord_yb_15": coord_yn_15,
        "coord_zb_15": coord_yn_15,

        "coord_tipo_16": coord_tipo_16,
        "coord_xn_16": coord_xn_16,
        "coord_yn_16": coord_yn_16,
        "coord_zn_16": coord_yn_16,
        "coord_xb_16": coord_yn_16,
        "coord_yb_16": coord_yn_16,
        "coord_zb_16": coord_yn_16,



    }

    coefvento = {

    }

    # criar uma coleção "user" na database "local" e inserir o objeto "navio" nessa coleção
    conn.local.user.insert_one(dict(navio))

    conn.local.coordenadas.insert_one(dict(coordenadas))
    conn.local.coefvento.insert_one(dict(coefvento))

    # retornar uma pagina html
    return RedirectResponse("/cadastrar_navio/", status_code=status.HTTP_302_FOUND)