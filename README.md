# 2024-Spring-AI-Final-Project
## Auto Roll Call system 自動點名系統
**Check out our demo video [here]!(https://google.com)**  
**[PPT](https://google.com)**  
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
   - Download our pretrained model [Here](https://drive.google.com/drive/folders/1uGKw-sEQPMBAY83QOGWZUzfY-P4qJJ3w?fbclid=IwAR2mu166VIUVfrZaYwvIwOucGJhMSoftllX6tS5yXc88umxVJT1Js86COcY)  
   - Train your own model by [this project](https://github.com/fish5524/AI_final)  
3. Put the model in ```/logs``` folder  
4. Put your own students picuture in ```/static/Classes/class0``` folder  
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
https://arxiv.org/pdf/1503.03832

"Deep Residual Learning for Image Recognition" https://arxiv.org/pdf/1512.03385

"Arc Face" https://arxiv.org/pdf/1801.07698  
