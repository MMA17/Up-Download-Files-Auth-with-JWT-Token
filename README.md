# Authenticate User with JWT Token

## Basic Upload/Download Files Python app authenticate user with JWT Token

### Login command
curl \
   -H 'Content-Type: application/json' \
   -d '{"username":"admin","password":"123456"}' \
   http://192.168.18.176:5000/token

### Upload File 
curl \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzM0ODUyMjksImlhdCI6MTYzMzM5ODgyOSwibmJmIjoxNjMzMzk4ODI5LCJ1c2VybmFtZSI6ImFkbWluIn0.SxRXUp2UaiOXTAMwFB_wy_Lb3RZGuBnZRRj7SPsUMFY' \
  -F "file=@./testfile2.txt" \
  http://192.168.18.176:5000/upload

### Download File
curl -O \
  -H 'token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzM0ODUyMjksImlhdCI6MTYzMzM5ODgyOSwibmJmIjoxNjMzMzk4ODI5LCJ1c2VybmFtZSI6ImFkbWluIn0.SxRXUp2UaiOXTAMwFB_wy_Lb3RZGuBnZRRj7SPsUMFY' \
  http://192.168.18.176:5000/download/testfile2.txt

