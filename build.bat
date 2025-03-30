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
    echo Virtual environment is already exists.
    echo Activating virtual environment...
    call %ENV_DIR%\Scripts\activate
)

:: Получаем путь к CustomTkinter
for /f "tokens=1,* delims=: " %%A in ('pip show customtkinter ^| findstr "Location:"') do set my_path=%%B

:: Убираем пробелы в начале (если есть)
set my_path=!my_path: =!

:: Заменяем обратные слэши на обычные
set my_path=!my_path:\=/!

:: Выводим путь к CustomTkinter
echo CustomTkinter path: !my_path!

:: Формируем и выполняем команду PyInstaller
set command=pyinstaller --noconfirm --windowed --icon=icon.ico --onefile --add-data "*.png;." --add-data "!my_path!/customtkinter;customtkinter/" app.py

echo Command running: !command!
%command%

pause
endlocal