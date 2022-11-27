from fastapi import FastAPI, Request 
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.routers import  \
    (
     health,
     books_route
     )
#from config import settings

app = FastAPI(
    title = 'Gutendex Search API',
    version='1.0.0',
)

# Allow CORS from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handle data model error
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": {
            "status": "Error",
            "description": "Wrong JSON input format"
        },
                 }),
    )

# Routers
app.include_router(health.router)
app.include_router(books_route.router)
