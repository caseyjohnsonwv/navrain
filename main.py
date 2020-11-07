from fastapi import FastAPI
from routers import login, healthcheck

app = FastAPI()
app.include_router(healthcheck.router)
app.include_router(login.router, prefix="/login")
