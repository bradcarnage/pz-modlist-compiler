@echo off
set "pyexec=none"
if exist %localappdata%\Programs\Python\Python311\python.exe (
    set "pyexec=%localappdata%\Programs\Python\Python311\python.exe"
)
if %pyexec%==none (
    echo COULD NOT FIND A COMPATIBLE PYTHON 3 VERSION
    echo Please visit https://python.org/ and download version 3.11
) else (
    echo === USING PYTHON EXEC: %pyexec%
    %pyexec% --version
    echo === PIP INSTALL REQUESTS
    %pyexec% -m pip install requests
    echo === RUNNING MAIN.PY
    %pyexec% main.py
)
pause