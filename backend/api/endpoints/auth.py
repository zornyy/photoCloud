from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from services.authentication import UserCreate, UserLogin, register_new_user, login_user

# Create router
router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    new_user = register_new_user(db, user_data)
    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "username": new_user.username
    }

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """Login a user."""
    token = login_user(db, user_data)
    return token