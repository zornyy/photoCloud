from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)  # Store hashed password, not plaintext
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationship to photos - one user can have many photos
    photos = relationship("Photo", back_populates="user", cascade="all, delete-orphan")
    
    # Optional: add storage quota if you want to limit storage per user
    storage_quota_mb = Column(Integer, default=1024, nullable=False)  # Default 1GB quota