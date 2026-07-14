import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "BankGuard AI"
    VERSION = "1.0.0"

    NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
    NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"

    MODEL_NAME = "meta/llama-3.1-8b-instruct"

    UPLOAD_FOLDER = "uploads"


settings = Settings()