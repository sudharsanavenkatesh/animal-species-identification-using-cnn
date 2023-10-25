import os
from flask import Flask, flash, request, redirect, url_for,send_from_directory, render_template
from werkzeug.utils import secure_filename
import t1 
import cv2 as cv

UPLOAD_FOLDER = "E:\\hac\\flak"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__,template_folder="template")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="./css/styles.css">
  <title>Animal Species Detection</title>
  <style>
        body{
         background-color:#FFFFE0
        }
        
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin-bottom: 20px;
}

  </style>
</head>
  <body>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file style="color:red;width:250px;height:40px;">
      <input type=submit value=Upload style="background-color:black;color:white;width:150px;height:40px;" >
    </form>
  </body>
</html>'''
@app.route('/uploads/<name>')
def download_file(name):
    pr=t1.pred(name)
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)