from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import search_router, config_router
from app.common.config import API_VERSION, VERSION
from app.schemas.result_schema import ResultDTO


app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir acceso desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)


@app.get("/about")
async def root():
    return JSONResponse(content={"version": VERSION, "api_version": API_VERSION, "author": "Lueyo"})

app.include_router(search_router.router, prefix=f"/api/v{API_VERSION}/search")
app.include_router(config_router.router, prefix=f"/api/v{API_VERSION}/config")