import time
import pytest
import jwt
import hashlib
from app.utils import security

SECRET = "test_secret"

def test_hash_password():
    """
    Verifica que la función hash_password retorne un hash de longitud 64 (para SHA256)
    y que coincida con el cálculo manual.
    """
    password = "mysecretpassword"
    hashed = security.hash_password(password)
    
    assert isinstance(hashed, str)
    assert len(hashed) == 64

    expected_hash = hashlib.sha256(password.encode()).hexdigest()
    assert hashed == expected_hash

def test_verify_password_correct():
    """
    Verifica que verify_password retorne True cuando la contraseña coincide con el hash.
    """
    password = "mysecretpassword"
    hashed = security.hash_password(password)
    assert security.verify_password(password, hashed) is True

def test_verify_password_incorrect():
    """
    Verifica que verify_password retorne False cuando la contraseña es incorrecta.
    """
    password = "mysecretpassword"
    wrong_password = "wrongpassword"
    hashed = security.hash_password(password)
    assert security.verify_password(wrong_password, hashed) is False

def test_generate_and_verify_token():
    """
    Genera un token con datos de ejemplo y verifica que:
      - Se retorne un token (cadena).
      - La verificación del token devuelva los datos originales.
      - El payload incluya el campo 'exp'.
    """
    data = {"user_id": 123, "role": "admin"}
    token = security.generate_token(data, SECRET, exp=60)
    
    assert isinstance(token, str)
    
    decoded = security.verify_token(token, SECRET)
    
    for key in data:
        assert decoded[key] == data[key]
    
    assert "exp" in decoded

def test_expired_token():
    """
    Genera un token con expiración muy corta y verifica que, pasado el tiempo
    se lance una excepción de token expirado.
    """
    data = {"user_id": 456}
    token = security.generate_token(data, SECRET, exp=1)
    
    time.sleep(2)
    
    with pytest.raises(jwt.ExpiredSignatureError):
        security.verify_token(token, SECRET)
