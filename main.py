from fastapi import FastAPI

import models
from database import engine
from auth import router as auth_router
from tasks import router as tasks_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Task Manager API with JWT Authentication",
    version="1.0.0"
)

# Include Routers
app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Task Manager API"
    }