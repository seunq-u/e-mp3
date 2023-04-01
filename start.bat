@echo off
chcp 65001
title E-Mp3

@REM start "lavalink" lavalink.bat

@REM timeout /t 7 /nobreak

.venv\Scripts\python.exe -u main.py
pause