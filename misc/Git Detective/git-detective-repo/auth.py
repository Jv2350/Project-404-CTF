import jwt
import hashlib
import secrets

SECRET_KEY = "super_secret_do_not_commit"

def generate_token(user_id):
    payload = {"user_id": user_id, "type": "session"}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return None

def hash_password(password):
    salt = secrets.token_hex(16)
    h = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{h}"
