from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, BigInteger
from sqlalchemy.orm import relationship
import os
from uuid import uuid4
from db.database import Base

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    # Using UUID in filename to avoid collisions
    filename = Column(String(255), unique=True, nullable=False)
    original_filename = Column(String(255), nullable=False)
    # Store relative path from uploads directory
    path = Column(String(255), nullable=False)
    # Store the full path for easier access
    full_path = Column(String(255), nullable=False)
    # Store file size in bytes
    file_size = Column(BigInteger, nullable=False)
    # Store file mime type
    mime_type = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    
    # Foreign key to link to user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationship to user - many photos belong to one user
    user = relationship("User", back_populates="photos")
    
    @staticmethod
    def generate_unique_filename(original_filename):
        """Generate a unique filename based on UUID and original extension"""
        _, file_extension = os.path.splitext(original_filename)
        return f"{uuid4().hex}{file_extension}"
    
    @classmethod
    def create_from_upload(cls, user_id, file_name, file_path, file_size, mime_type):
        """Create a new photo record from an uploaded file"""
        unique_filename = cls.generate_unique_filename(file_name)
        # Create relative path from uploads directory
        relative_path = f"user_{user_id}/{unique_filename}"
        # Full path for file system operations
        full_path = os.path.join("/uploads", relative_path)
        
        return cls(
            name=file_name,
            filename=unique_filename,
            original_filename=file_name,
            path=relative_path,
            full_path=full_path,
            file_size=file_size,
            mime_type=mime_type,
            user_id=user_id
        )