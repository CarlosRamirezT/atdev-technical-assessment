import os
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Validates the provided username and password against the values stored in the environment variables.
    """
    correct_username = os.getenv("API_USER")
    correct_password = os.getenv("API_PWD")
    
    if not (credentials.username == correct_username and credentials.password == correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
