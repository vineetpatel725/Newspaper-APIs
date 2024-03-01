from fastapi import FastAPI

from app.routes import newspaper_router

app: FastAPI = FastAPI(title="FastaAPI With Celery")

app.include_router(newspaper_router)
