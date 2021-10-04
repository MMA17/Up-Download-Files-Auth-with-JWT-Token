import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template,session,Response
from tokens import checkToken, genToken


UPLOAD_FOLDER = 'uploads/'
#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/token')

@app.route('/token', methods=['GET', 'POST'])
def gettoken():
    header = dict(request.headers)
    data = request.get_json()
    # print (header)
    # print (request.headers.get('token'))
    
    if data['username'] == "admin" and data['password'] == "123456":
        token = genToken(data['username'])
        print (token)
        return token
    return "Sai ten dang nhap hoac mat khau"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    header = dict(request.headers)
    token = request.headers.get('token')
    print(header)
    print(token)
    result = checkToken(token)
    print(result)
    if result == "Token dung":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Tai len thanh cong"
    return "Tai len that bai"

@app.route('/download/<filename>')
def download(filename):
    token = request.headers.get('token')
    result = checkToken(token)
    if result == "Token dung":
        file_path = UPLOAD_FOLDER + filename
        return send_file(file_path, as_attachment=True, attachment_filename=filename)
    return "Xac thuc that bai"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')