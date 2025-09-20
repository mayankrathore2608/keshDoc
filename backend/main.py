import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import symptoms
from database.database import create_tables

app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

app.include_router(symptoms.router, prefix=settings.API_PREFIX)

app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")


# ✅ Optional: Serve index.html explicitly
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_path, "index.html"))


create_tables()

# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
