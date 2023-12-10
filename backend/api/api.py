from fastapi import FastAPI
from .modules import drought#, flood, landslide, wildfire
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://happy-field-07211a803.4.azurestaticapps.net/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.router.include_router(drought.router)
# app.router.include_router(flood.router)
# app.router.include_router(landslide.router)
# app.router.include_router(wildfire.router)