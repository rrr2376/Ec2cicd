from fastapi import APIRouter, HTTPException
from app.schemas.auth import TokenResponse, RefreshRequest
from app.core.security import create_access_token, create_refresh_token
from app.services.auth_service import refresh_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login():
    user_id = "123"
    return {
        "access_token": create_access_token({"sub": user_id}),
        "refresh_token": create_refresh_token({"sub": user_id})
    }

@router.post("/refresh")
def refresh_token(request: RefreshRequest):
    new_token = refresh_access_token(request.refresh_token)

    if not new_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    return {"access_token": new_token}
