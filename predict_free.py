import numpy as np
from PIL import Image
import cv2
import insightface
from insightface.app import FaceAnalysis
from siamese import Siamese

def write_face_to_tmp(file_path):
    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    img = cv2.imread(file_path)
    faces = app.get(img)
    i = 0
    for face in faces:
        i = i + 1
        x1, y1, x2, y2 = face.bbox.astype(int)
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(img.shape[1], x2), min(img.shape[0], y2)
        face_img = img[y1:y2, x1:x2]
        
        # 保存裁剪出的人臉圖片
        face_filename = f'./tmp/face_{i}.jpg'
        cv2.imwrite(face_filename, face_img)
        print(f'Saved face image: {face_filename}')
        
    return i # return how many faces in the pic

def get_sim(img1_path, img2_path):
    model = Siamese()
    image_1 = Image.open(img1_path)
    image_2 = Image.open(img2_path)
    probability = model.detect_image(image_1,image_2)
    return probability
