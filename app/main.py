from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import tempfile
import os

from app.ai_model import analyze_image


app = FastAPI(
    title="AzureVision-AI",
    description="AI-powered image analysis application",
    version="1.0.0"
)


# Serve frontend files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    if file.content_type not in allowed_types:
        return {
            "success": False,
            "error": "Please upload a JPG, PNG, or WEBP image."
        }

    contents = await file.read()

    temporary_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    try:
        temporary_file.write(contents)
        temporary_file.close()

        results = analyze_image(
            temporary_file.name
        )

        return {
            "success": True,
            "filename": file.filename,
            "predictions": results
        }

    finally:
        if os.path.exists(temporary_file.name):
            os.remove(temporary_file.name)