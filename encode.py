import jwt
import datetime, time
from cryptography.hazmat.primitives import serialization
from jwt.exceptions import ExpiredSignatureError

key = "123456"
payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'nbf': datetime.datetime.utcnow(),
            'sub': "111"
        }

print(payload)

token = jwt.encode(payload, key, algorithm="HS256",)
print(token)

decoded = jwt.decode(token, key="123456", algorithms="HS256")

print(decoded)

# print(datetime.datetime.utcnow().utcfromtimestamp())
# print (datetime.datetime.utcfromtimestamp(1633058702))

timestamp = time.mktime(datetime.datetime.utcnow().timetuple())
print(timestamp)

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzMwNTk3MTQsImlhdCI6MTYzMzA1OTcwOSwic3ViIjoiMTExIn0.BKwG_ZcxKrDYwHO_Dr3bvCJ0fIxwbv4GvdnPZ-FnXr0"
header_data = jwt.get_unverified_header(token)
print (header_data)
try:
    print(jwt.decode(token, key, algorithms="HS256"))
except ExpiredSignatureError as error:
    print(error)
