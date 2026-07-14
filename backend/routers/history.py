from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from services.database_service import DatabaseService

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def history(request: Request):

    history = DatabaseService.get_all()

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "request": request,
            "title": "History Analisis",
            "history": history
        }
    )