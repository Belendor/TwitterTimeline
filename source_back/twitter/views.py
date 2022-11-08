from random import randint
from flask import Blueprint
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from pymongo import MongoClient

cwd = os.getcwd()

UPLOAD_FOLDER = cwd + '\\uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

views = Blueprint('views', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/', methods=['Get', 'Post'])
def home():
    if request.method == 'GET':
        return 'works'
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

    client = MongoClient('mongodb://localhost:27017/')

    db = client['twitter']
    collection = db['twitter']

    collection.insert_one({'_id': randint(1,100),"title": request.form['title'], "date": request.form['date'][:10], "file_name": file.filename, 'sent': False})
    
    return {'status': 'ok'}
