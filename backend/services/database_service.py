from database.database import SessionLocal
from database.models import AnalysisHistory


class DatabaseService:

    @staticmethod
    def save(
        filename,
        summary,
        risk,
        analysis
    ):

        db = SessionLocal()

        data = AnalysisHistory(
            filename=filename,
            summary=summary,
            risk=risk,
            analysis=analysis
        )

        db.add(data)
        db.commit()
        db.close()

    @staticmethod
    def get_all():

        db = SessionLocal()

        data = (
            db.query(AnalysisHistory)
            .order_by(AnalysisHistory.id.desc())
            .all()
        )

        db.close()

        return data

    @staticmethod
    def get_dashboard_stats():

        db = SessionLocal()

        total = db.query(AnalysisHistory).count()

        high = db.query(AnalysisHistory).filter(
            AnalysisHistory.risk == "HIGH"
        ).count()

        medium = db.query(AnalysisHistory).filter(
            AnalysisHistory.risk == "MEDIUM"
        ).count()

        critical = db.query(AnalysisHistory).filter(
            AnalysisHistory.risk == "CRITICAL"
        ).count()

        db.close()

        return {
            "total": total,
            "threat": high + medium + critical,
            "high": high,
            "critical": critical
        }