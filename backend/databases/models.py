from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Time,
    Date,
    ARRAY,
)

from datetime import datetime

from .base import Base


class BaseModel(Base):
    __abstract__ = True
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class PostInfo(BaseModel):
    __tablename__ = "post_info"
    title = Column(String, nullable=False)
    section = Column(String, nullable=False)
    continuous_recruit = Column(Boolean, nullable=False, default=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=False)
    full_time = Column(Boolean, nullable=False, default=True)
    specific = Column(Boolean, nullable=False, default=True)
    task = Column(String, nullable=True)
    weekdays = Column(Boolean, nullable=False, default=True)
    work_start = Column(
        Time, nullable=False, default=datetime.strptime("09:00", "%H:%M").time()
    )
    work_end = Column(
        Time, nullable=False, default=datetime.strptime("18:00", "%H:%M").time()
    )
    work_spot = Column(
        String, nullable=True, default="서울시 금천구 가산디지털단지역 800m 이내"
    )
    apply_online_url = Column(String, nullable=True)  # 여기서 String으로 변경
    deleted = Column(Boolean, nullable=False, default=False)
    qualification = Column(String, nullable=True)  # 여기서 String으로 변경
    preferred = Column(String, nullable=True)  # 여기서 String으로 변경


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(Date, nullable=True)
    updated_at = Column(Date, nullable=True)
