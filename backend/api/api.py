from fastapi import FastAPI
from .modules import drought, flood, landslide, wildfire, markers
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://happy-field-07211a803.4.azurestaticapps.net",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.router.include_router(drought.router)
app.router.include_router(flood.router)
app.router.include_router(landslide.router)
app.router.include_router(wildfire.router)
app.router.include_router(markers.router)