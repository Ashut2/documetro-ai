from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# sqlitte databse url
DATABASE_URL = "sqlite:///./test.db"
# Engin = actual connection to DB
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Session = used to talk to DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for our ORM models
Base = declarative_base()
# ORM models for "documents" table
class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    filepath = Column(String)
# Create table if not exists
Base.metadata.create_all(bind=engine)

#  Dependency for FastAPI routes
def get_db():
    """
    Dependency that creates a new DB session for each request,
    and closes it after the request is done.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
