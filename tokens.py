import jwt
import datetime, time
from cryptography.hazmat.primitives import serialization
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

secret_key = "123456"

def genToken(username):
    payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'nbf': datetime.datetime.utcnow(),
            'username': username
        }
    token = jwt.encode(payload, secret_key, algorithm="HS256",)
    
    return token

def checkToken(token):
    try:
        decoded = jwt.decode(token, key=secret_key, algorithms="HS256")
        # if decoded['username'] == username:
        #     return "Token dung"
    except ExpiredSignatureError:
        return 101
    except InvalidSignatureError:
        return 102
    except:
        return 103
    return 100
