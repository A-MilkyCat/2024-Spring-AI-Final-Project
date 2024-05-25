from flask import Flask, render_template, request, redirect, url_for, session
import os
import random
import test
import check_face

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # secret key for your session
UPLOAD_FOLDER = 'static/uploads/'
CLASS_FOLDER = 'static/Classes/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_students(class_name):
    class_path = os.path.join(CLASS_FOLDER, class_name)
    return [
        {'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': False}
        for f in os.listdir(class_path)
        if f.endswith('.jpg') or f.endswith('.png')
    ]
def get_students_absent(class_name, file_path):
    threshold = 0.4
    class_path = os.path.join(CLASS_FOLDER, class_name)
    students = []
    for f in os.listdir(class_path):
        if f.endswith('.jpg') or f.endswith('.png'):
            sim = check_face.get_sim(file_path, os.path.join(class_path, f), threshold)
            if sim >= threshold:
                students.append({'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': True })
            else:
                students.append({'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': False })
    return students

@app.route('/', methods=['GET', 'POST'])
def index():
    classes = os.listdir(CLASS_FOLDER)
    selected_class = request.args.get('class', session.get('selected_class', classes[0] if classes else None))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            print(file_path)
            file.save(file_path)
            # students = session.get('students', get_students_absent(selected_class, file_path))
            students = get_students_absent(selected_class, file_path)
            session['students'] = students
            return redirect(url_for('index', uploaded_image=file.filename))

    if 'students' not in session or session.get('selected_class') != selected_class:
        students = get_students(selected_class)
        session['students'] = students
        session['selected_class'] = selected_class
    else:
        students = session['students']
    
    uploaded_image = request.args.get('uploaded_image', None)
    return render_template('index.html', classes=classes, selected_class=selected_class, students=students, uploaded_image=uploaded_image)

if __name__ == '__main__':
    app.run(debug=True)
