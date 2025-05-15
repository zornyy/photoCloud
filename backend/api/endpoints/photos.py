from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
import os
import shutil
from pathlib import Path

from db.database import get_db
from models.photo import Photo
from services.authentication import get_current_active_user
from models.user import User
from middleware.jwt_middleware import jwt_bearer

# Create router
router = APIRouter(
    prefix="/photos",
    tags=["photos"],
    dependencies=[Depends(jwt_bearer)]  # Protect all routes with JWT
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_photo(
    file: UploadFile = File(...),
    name: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Upload a new photo."""
    # Validate file type (e.g., only allow images)
    valid_content_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
    if file.content_type not in valid_content_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Only {', '.join(valid_content_types)} are allowed."
        )
    
    # Create user directory if it doesn't exist
    user_dir = Path(f"./uploads/user_{current_user.id}")
    user_dir.mkdir(parents=True, exist_ok=True)
    
    # Calculate file size
    file.file.seek(0, 2)  # Seek to end of file
    file_size = file.file.tell()  # Get current position (file size)
    file.file.seek(0)  # Reset to beginning of file
    
    # Check if user has enough quota
    total_used = db.query(Photo).filter(Photo.user_id == current_user.id).with_entities(func.sum(Photo.file_size)).scalar() or 0
    if (total_used + file_size) > (current_user.storage_quota_mb * 1024 * 1024):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Storage quota exceeded"
        )
    
    # Create photo record
    photo = Photo.create_from_upload(
        user_id=current_user.id,
        file_name=name,
        file_path=file.filename,
        file_size=file_size,
        mime_type=file.content_type
    )
    
    # Create full directory path if it doesn't exist
    os.makedirs(os.path.dirname(photo.full_path), exist_ok=True)
    
    # Save the file
    with open(photo.full_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Save the photo record to database
    db.add(photo)
    db.commit()
    db.refresh(photo)
    
    return {
        "id": photo.id,
        "name": photo.name,
        "size": photo.file_size,
        "path": photo.path
    }

@router.get("/")
def get_user_photos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all photos for the current user."""
    photos = db.query(Photo).filter(Photo.user_id == current_user.id).all()
    return photos

@router.get("/{photo_id}")
def get_photo_by_id(
    photo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific photo by ID."""
    photo = db.query(Photo).filter(Photo.id == photo_id, Photo.user_id == current_user.id).first()
    
    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Photo not found"
        )
    
    return photo

@router.delete("/{photo_id}")
def delete_photo(
    photo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete a photo."""
    photo = db.query(Photo).filter(Photo.id == photo_id, Photo.user_id == current_user.id).first()
    
    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Photo not found"
        )
    
    # Delete the file
    try:
        os.remove(photo.full_path)
    except OSError:
        pass  # File might not exist, continue anyway
    
    # Delete the record
    db.delete(photo)
    db.commit()
    
    return {"message": "Photo deleted successfully"}