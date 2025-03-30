@echo off
setlocal enabledelayedexpansion
set ENV_DIR=ENV

if not exist %ENV_DIR% (
    echo Creating virtual environment...
    python -m venv %ENV_DIR%

    echo Activating virtual environment...
    call %ENV_DIR%\Scripts\activate

    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
    echo Ready! Virtual environment is set up.
) else (
    echo Virtual environment already exists.
    echo Activating virtual environment...
    call %ENV_DIR%\Scripts\activate
)

for /f "tokens=1,* delims=: " %%A in ('pip show customtkinter ^| findstr "Location:"') do set my_path=%%B
set my_path=!my_path: =!
set my_path=!my_path:\=/!
echo CustomTkinter path: !my_path!
set command=pyinstaller --noconfirm --windowed --icon=icon.ico --onefile --add-data "*.png;." --add-data "!my_path!/customtkinter;customtkinter/" app.py
echo Command running: !command!
%command%
echo Waiting for PyInstaller to finish...
timeout /t 3 /nobreak >nul

if exist dist (
    echo Renaming dist to builded...
    rename dist builded
)

if exist build (
    echo Deleting build folder...
    rmdir /s /q build
)

if exist app.spec (
    echo Deleting app.spec...
    del app.spec
)

echo Done!
pause
endlocal
