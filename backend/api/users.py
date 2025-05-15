from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from db.database import get_db
from schemas.user import LoginRequest


router = APIRouter()

@router.post("/login")
def login(request: LoginRequest, db = Depends(get_db)):
    return {
        "message": "Called login endpoint"
    }
