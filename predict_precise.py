import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis

def get_sim(file_path, student_path, threshold):

    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    handler = insightface.model_zoo.get_model('C:/Users/User/.insightface/models/buffalo_l/w600k_r50.onnx') # find your own model path
    handler.prepare(ctx_id=0)

    img1 = cv2.imread(file_path) # big pic
    img2 = cv2.imread(student_path)

    faces = app.get(img1)
    student_face = app.get(img2)[0]

    t = 1
    for face in faces:
        feat1 = handler.get(img1, face)
        student_feat = handler.get(img2, student_face)
        sim = handler.compute_sim(feat1, student_feat)
        t = t+1
        if (sim >= threshold):
            print(t, sim)
            return sim
    return 0

# rimg = app.draw_on(img, faces)
# cv2.imwrite("./t2_output.jpg", rimg)