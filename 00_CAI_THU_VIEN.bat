@echo off
setlocal EnableExtensions
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
 set "PY=.venv\Scripts\python.exe"
) else if exist "..\.venv\Scripts\python.exe" (
 set "PY=..\.venv\Scripts\python.exe"
) else (
 python -m venv .venv
 if errorlevel 1 goto fail
 set "PY=.venv\Scripts\python.exe"
)
"%PY%" -m pip install --upgrade pip
if errorlevel 1 goto fail
"%PY%" -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 goto fail
echo [OK] Cai dat xong. Mo 01_CHAY_LOCAL_V13.bat de chay web.
pause
exit /b 0
:fail
echo [LOI] Cai dat chua thanh cong. Gui anh thong bao loi phia tren.
pause
exit /b 1
