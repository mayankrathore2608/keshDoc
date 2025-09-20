from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import symptoms
from database.database import create_tables

app = FastAPI(title="KeshDoc : Your Hair's Friend", version="0.0.1",
              description="Building Kesh Doc APIs", docs_url="/docs", redoc_url="/redocs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

print(settings.API_PREFIX)
app.include_router(symptoms.router,prefix=settings.API_PREFIX)
create_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
