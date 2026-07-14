from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database.database import engine
from database.models import Base

from config import settings
from services.database_service import DatabaseService
from routers.analyze import router as analyze_router
from routers.history import router as history_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="LLM Banking Security Analyzer"
)

Base.metadata.create_all(bind=engine)

app.include_router(analyze_router)
app.include_router(history_router)

# Folder static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Folder template
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    stats = DatabaseService.get_dashboard_stats()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "title": settings.APP_NAME,

            "stats": stats,

            "filename": None,
            "summary": None,
            "threat": [],
            "risk": None,
            "evidence": [],
            "recommendation": []
        }
    )


@app.get("/health")
async def health():
    return {
        "status": "OK",
        "app": settings.APP_NAME,
        "version": settings.VERSION
    }