@echo off
chcp 65001
title E-Mp3

start "lavalink" lavalink.bat

timeout /t 7 /nobreak

.venv\Scripts\python.exe -u main.py