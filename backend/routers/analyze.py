from fastapi import APIRouter, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import shutil
import os

from services.analyzer import Analyzer
from services.database_service import DatabaseService

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"]
)

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_log(
    request: Request,
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = Analyzer.analyze(file_path)

    stats = DatabaseService.get_dashboard_stats()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "title": "BankGuard AI",

            "stats": stats,

            "filename": file.filename,

            "summary": result.get("summary", ""),

            "threat": result.get("threat", []),

            "risk": result.get("risk", "UNKNOWN"),

            "evidence": result.get("evidence", []),

            "recommendation": result.get("recommendation", [])
        }
    )


@router.get("/download/{filename}")
async def download_pdf(filename: str):

    pdf_path = f"reports/{filename}.pdf"

    return FileResponse(
        path=pdf_path,
        filename=f"{filename}.pdf",
        media_type="application/pdf"
    )