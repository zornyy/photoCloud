from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import ValidationError
import jwt

from core.config import settings
from services.authentication import TokenData

class JWTBearer(HTTPBearer):
    """
    JWT Bearer token authentication middleware.
    This middleware will validate the JWT token in the Authorization header.
    """
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication scheme.",
                )
            
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token or expired token.",
                )
            
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authorization code.",
            )

    def verify_jwt(self, token: str) -> bool:
        """
        Verify the JWT token.
        """
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            
            # Validate token data
            token_data = TokenData(username=payload.get("sub"), user_id=payload.get("user_id"))
            
            return True if token_data.username and token_data.user_id else False
            
        except (jwt.PyJWTError, ValidationError):
            return False


# Create an instance of the middleware
jwt_bearer = JWTBearer()