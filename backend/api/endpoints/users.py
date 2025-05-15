from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from services.authentication import get_current_active_user
from models.user import User
from middleware.jwt_middleware import jwt_bearer

# Create router
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(jwt_bearer)]  # Protect all routes with JWT
)

@router.get("/me")
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Get current user information."""
    return {
        "id": current_user.id,
        "username": current_user.username,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "storage_quota_mb": current_user.storage_quota_mb
    }

@router.put("/me")
def update_user_info(
    full_name: str = None,
    email: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update current user information."""
    # Update fields if provided
    if full_name is not None:
        current_user.full_name = full_name
    if email is not None:
        # Check if email already exists for another user
        existing_user = db.query(User).filter(User.email == email, User.id != current_user.id).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        current_user.email = email
    
    # Save changes
    db.commit()
    db.refresh(current_user)
    
    return {
        "id": current_user.id,
        "username": current_user.username,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "storage_quota_mb": current_user.storage_quota_mb
    }