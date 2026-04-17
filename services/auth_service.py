from jose import jwt, JWTError
from app.core.config import settings
from app.core.security import create_access_token

def refresh_access_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")

        if not user_id:
            return None

        return create_access_token({"sub": user_id})

    except JWTError:
        return None
