from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.config import settings
from routers import symptoms
from database.database import create_tables

app = FastAPI(title="KeshDoc : Your Hair's Friend", version="0.0.1",
              description="Building Kesh Doc APIs", docs_url="/docs", redoc_url="/redocs")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOWED_ORIGINS,
#     allow_credentials=True,
#     allow_headers=["*"],
#     allow_methods=["*"]
# )

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_path, "index.html"))


app.include_router(symptoms.router, prefix=settings.API_PREFIX)
create_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
