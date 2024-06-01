# 2024-Spring-AI-Final-Project
## Auto Roll Call system 自動點名系統
**Check out our demo video [here](https://google.com)!**  
**[PPT]([https://google.com](https://docs.google.com/presentation/d/1TjFuRr5vVuy6mjkHQ2ntSJ5wVJuoA7EmUwdwKCe0xV4/edit?usp=sharing))**  
## Introduction
This project create a local Auto Roll Call system with a simple interface.  
You can check whether the students are absent by uplaod a picture.  
There are two roll call methods:
- ```free.py``` this 
- ```precise.py```
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
   - Train your own model by [this project](https://github.com/fish5524/AI_final)  
3. Put the model in ```/logs``` folder  
### Prepare your students picture 
Put your students picuture in ```/static/Classes/class0``` folder  
You can also create a new class folder  under ```/static/Classes```  
## Usage
Depend on your need, Run  
```
python free.py
```
or  
```
python precise.py
```
then go to website  
```
http://127.0.0.1:5000/
```
## Reference
"FaceNet: A Unified Embedding for Face Recognition and Clustering" https://arxiv.org/pdf/1503.03832

"Deep Residual Learning for Image Recognition" https://arxiv.org/pdf/1512.03385

"Arc Face" https://arxiv.org/pdf/1801.07698

Dataset : https://www.kaggle.com/datasets/atulanandjha/lfwpeople

Insightface : https://github.com/deepinsight/insightface

siamese network : https://github.com/bubbliiiing/Siamese-pytorch/tree/master

