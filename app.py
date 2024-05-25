from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
CLASS_FOLDER = 'static/Classes/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CLASS_FOLDER'] = CLASS_FOLDER
@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded_image = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            uploaded_image = file.filename
            
            return redirect(url_for('index', uploaded_image=uploaded_image))
    
    
    classes = os.listdir(CLASS_FOLDER)
    
    selected_class = request.args.get('class', classes[0] if classes else None)
    students = []
    if selected_class:
        class_path = os.path.join(CLASS_FOLDER, selected_class)
        students = [
            {'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': random.choice([True, False])} 
            for f in os.listdir(class_path) 
            if f.endswith('.jpg') or f.endswith('.png')
        ]
        
    uploaded_image = request.args.get('uploaded_image', None)
    return render_template('index.html', classes=classes, selected_class=selected_class, students=students, uploaded_image=uploaded_image)

if __name__ == '__main__':
    app.run(debug=True)
