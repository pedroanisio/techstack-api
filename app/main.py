from fastapi import FastAPI
from .routes import router
from .database import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)
