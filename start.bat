@echo off
set FLASK_APP=app.py
start cmd /k flask run
start http://127.0.0.1:5000