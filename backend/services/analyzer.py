from services.log_parser import LogParser
from services.nvidia_service import NvidiaService
from services.database_service import DatabaseService
from services.pdf_service import PDFService


class Analyzer:

    @staticmethod
    def analyze(file_path: str):

        # Membaca isi file log
        log_content = LogParser.parse(file_path)
        # Batasi maksimal 200 baris
        log_content = "\n".join(
            log_content.splitlines()[:200]
        )

        # Hasil dari NVIDIA (sudah berupa dictionary)
        ai_result = NvidiaService.analyze(log_content)

        # Ambil data dari JSON
        summary = ai_result.get("summary", "")
        threat = ai_result.get("threat", [])
        risk = ai_result.get("risk", "UNKNOWN")
        evidence = ai_result.get("evidence", [])
        recommendation = ai_result.get("recommendation", [])

        # Simpan ke database
        DatabaseService.save(
            filename=file_path.split("/")[-1],
            summary=summary,
            risk=risk,
            analysis=str(ai_result)
        )

        # Generate PDF
        PDFService.generate(
            file_path.split("/")[-1],
            {
                "summary": summary,
                "threat": threat,
                "risk": risk,
                "evidence": evidence,
                "recommendation": recommendation
            }
        )

        # Debug hasil AI
        print("===== HASIL AI =====")
        print(summary)
        print(threat)
        print(risk)
        print(evidence)
        print(recommendation)
        print("====================")

        # Kirim ke frontend
        return {
            "summary": summary,
            "threat": threat,
            "risk": risk,
            "evidence": evidence,
            "recommendation": recommendation
        }