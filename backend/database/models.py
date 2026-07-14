from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database.database import Base


class AnalysisHistory(Base):

    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    risk = Column(String)
    summary = Column(String)
    analysis = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)