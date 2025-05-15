from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from db.database import get_db

router = APIRouter()

@router.post("AddImage")
def login(db = Depends(get_db)):
    return {
        "message": "Called login endpoint"
    }
