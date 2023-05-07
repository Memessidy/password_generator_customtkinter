# password_generator_customtkinter
simple password generator with ui on customtkinter

you need to install pyinstaller before building:
pip install pyinstaller

Your customtkinter location:
pip show customtkinter

command:
pyinstaller --noconfirm --windowed --icon=icon.ico --onefile --add-data "*.png;." --add-data "<CustomTkinter Location>/customtkinter;customtkinter/" app.py
