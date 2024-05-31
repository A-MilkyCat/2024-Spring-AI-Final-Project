from flask import Flask, render_template, request, redirect, url_for, session
import os
import predict_free
import test

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
    counts = test.show_face(file_path)
    class_path = os.path.join(CLASS_FOLDER, class_name)
    students = []
    num = predict_free.write_face_to_tmp(file_path)
    #special case: people in the pic more than student: everyone check
    if (num >= len(os.listdir(class_path))):
        return [
            {'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': True}
            for f in os.listdir(class_path)
            if f.endswith('.jpg') or f.endswith('.png')
        ]
    # for i in range(1, num+1):
    i = 0
    print(num)
    attend = predict_free.get_sim("tmp", class_path, num)
    for f in os.listdir(class_path):
        if f.endswith('.jpg') or f.endswith('.png'):
            students.append({'name': f.split('.')[0], 'image': os.path.join(class_path, f), 'present': True if i in attend else False })
            # counts = counts -1
        i = i + 1
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
            # 上传图片后随机确认学生出席
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
