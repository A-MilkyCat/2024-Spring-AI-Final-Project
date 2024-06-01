import numpy as np
from PIL import Image
import cv2
from insightface.app import FaceAnalysis
from siamese import Siamese
import os
import matplotlib.pyplot as plt

def write_face_to_tmp(file_path):
    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    img = cv2.imread(file_path)
    faces = app.get(img)
    i = 0
    extend_const = 0.1
    for face in faces:
        i = i + 1
        x1, y1, x2, y2 = face.bbox.astype(int)
        x_dif = x2 - x1
        y_dif = y2 - y1
        x1, y1 = max(0, x1-int(extend_const*x_dif)), max(0, y1-int(extend_const*y_dif))
        x2, y2 = min(img.shape[1], x2+int(extend_const*x_dif)), min(img.shape[0], y2+int(extend_const*y_dif))
        face_img = img[y1:y2, x1:x2]
        
        face_filename = f'./tmp/face_{str(i//10) + str(i%10) }.jpg'
        cv2.imwrite(face_filename, face_img)
        # print(f'Saved face image: {face_filename}')
        
    return i # return how many faces in the pic

def get_sim(file_path, student_path, num):
    model = Siamese()

    member_img = []
    for f in os.listdir(student_path):
        if f.endswith('.jpg') or f.endswith('.png'):
            member_path = os.path.join(student_path, f)
            img = Image.open(member_path)
            member_img.append(img)
            

    student_img = []
    students_path = file_path
    for student in os.listdir(students_path):
        if student.endswith('.jpg') or student.endswith('.png'):
            student_path = os.path.join(students_path, student)
            img = Image.open(student_path)
            student_img.append(img)
            num = num - 1
            if (num == 0):
                break

    Score = np.zeros((len(student_img), len(member_img)))

    for i in range(len(student_img)):
        for j in range(len(member_img)):
            probability = model.detect_image(student_img[i],member_img[j])
            Score[i][j] = probability.item()
    # print(Score)
    
    sx = {}
    sy = {}
    while(True):
        row_col_index=np.unravel_index(np.argmax(Score),Score.shape)
        x = row_col_index[0]
        y = row_col_index[1]
        if x not in sx and y not in sy:
            sx[x] = Score[x][y]
            sy[y] = Score[x][y]
            # plt.subplot(1, 2, 1)
            # plt.imshow(np.array(student_img[x]))

            # plt.subplot(1, 2, 2)
            # plt.imshow(np.array(member_img[y]))
            # plt.text(-12, -12, 'Similarity:%.3f' % Score[x][y], ha='center', va= 'bottom',fontsize=11)
            # plt.show()
        Score[x][y] = 0
        if len(sx) == len(student_img):
            break
    # sx = dict(sorted(sx.items()))
    # sy = dict(sorted(sy.items()))
    # print(sx)
    return sy.keys() # return a list 
    print(sy)
    model = Siamese()
    image_1 = Image.open(img1_path)
    image_2 = Image.open(img2_path)
    probability = model.detect_image(image_1,image_2)
    return probability
