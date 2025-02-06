import hashlib
import time
import jwt

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hash_val: str) -> bool:
    return hash_password(password) == hash_val

def generate_token(data: dict, secret: str, algorithm: str = "HS256", exp: int = 3600) -> str:
    payload = data.copy()
    payload["exp"] = time.time() + exp
    return jwt.encode(payload, secret, algorithm=algorithm)

def verify_token(token: str, secret: str, algorithms: list = ["HS256"]) -> dict:
    return jwt.decode(token, secret, algorithms=algorithms)
