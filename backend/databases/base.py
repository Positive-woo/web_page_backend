# base.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "sqlite:///./recruit_data.db"  # 사용하고자 하는 데이터베이스 URL로 변경하세요.
)

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# 세션 로컬 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 선언적 베이스 클래스 생성
Base = declarative_base()


# 데이터베이스 세션을 가져오는 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
