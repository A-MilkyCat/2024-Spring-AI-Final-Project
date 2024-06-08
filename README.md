# Auto Roll Call system 自動點名系統
## Introduction
This project create a local Auto Roll Call system using siamese network with a simple interface as follows.  

<img src="https://github.com/A-MilkyCat/2024-Spring-AI-Final-Project/blob/trivial/static/Classes/Mayday/pic/demo1.png" width="650">  
  
<img src="https://github.com/A-MilkyCat/2024-Spring-AI-Final-Project/blob/trivial/static/Classes/Mayday/pic/demo2.png" width="650">  

You can check the attendance by taking a photo and uploading it.  
There are two roll call methods:
- ```free.py``` Assume all people in the photo are in the students list, students with highest similarity  will be considered present.
- ```precise.py``` Attendance is confirmed only if the similarity between the person in the photo and the person in the student list exceeds the threshold (Using Insightface model, more time consuming).
## Before Starting
### Clone this repo
```
git clone https://github.com/A-MilkyCat/2024-Spring-AI-Final-Project.git
```
### Install prerequisites
1. For python
```
pip install -r requirements.txt
```
2. Get the model by  
   - Download our pretrained model [Here](https://drive.google.com/file/d/10uY-Wbg71nDSsKxRduoUBIazWRFdW7I4/view?usp=sharing)  
   - Train your own model by [this project](https://github.com/bubbliiiing/Siamese-pytorch/tree/master)  
3. Put the model in ```/logs``` folder  
### Prepare your students list 
Put your students headshot in ```/static/Classes/class0``` folder  
You can also create a new class folder  under ```/static/Classes```  
## Usage
1. Depend on your need, Run  
```
python free.py
```
or  
```
python precise.py
```
2. go to website  
```
http://127.0.0.1:5000/
```
## Reference
"FaceNet: A Unified Embedding for Face Recognition and Clustering" https://arxiv.org/pdf/1503.03832

"Deep Residual Learning for Image Recognition" https://arxiv.org/pdf/1512.03385

"Arc Face" https://arxiv.org/pdf/1801.07698

Training Dataset : https://www.kaggle.com/datasets/atulanandjha/lfwpeople

Insightface : https://github.com/deepinsight/insightface

siamese network : https://github.com/bubbliiiing/Siamese-pytorch/tree/master

Siamese-pytorch: https://github.com/bubbliiiing/Siamese-pytorch/tree/master
