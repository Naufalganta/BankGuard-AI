import json
import time
from openai import OpenAI

from config import settings
from core.prompt import SYSTEM_PROMPT


client = OpenAI(
    base_url=settings.NVIDIA_BASE_URL,
    api_key=settings.NVIDIA_API_KEY
)


class NvidiaService:

    @staticmethod
    def analyze(log_text: str):

        start = time.time()

        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": log_text
                }
            ],
            temperature=0.2,
            max_tokens=700
        )

        end = time.time()

        print(f"⏱ NVIDIA selesai dalam {end - start:.2f} detik")

        ai_text = response.choices[0].message.content.strip()

        try:
            return json.loads(ai_text)

        except Exception:

            return {
                "summary": "AI mengembalikan format yang tidak valid.",
                "threat": [],
                "risk": "UNKNOWN",
                "evidence": [],
                "recommendation": [],
                "raw": ai_text
            }