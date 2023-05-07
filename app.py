import customtkinter
from password import create_new
import pyperclip
from PIL import Image
import os
import sys

if getattr(sys, 'frozen', False):
    # Running in a PyInstaller bundle
    base_path = sys._MEIPASS
else:
    # Running in normal Python environment
    base_path = os.path.abspath(".")

image_path = os.path.join(base_path, "password_generator.png")


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.values = values
        self.title = title
        self.checkboxes = []
        self.params = {'row': 1, 'padx': 5, 'pady': (5, 0), "sticky": "w"}

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(column=i, **self.params)
            self.checkboxes.append(checkbox)

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray60", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=len(self.checkboxes))

        self.password_length_slider = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=100,
                                                              command=self.slider_event)
        self.password_length_slider.grid(row=2, pady=(20, 20), sticky='ew', columnspan=len(self.checkboxes)-1)

        self.password_length_entry = customtkinter.CTkEntry(self, width=30)
        self.password_length_entry.grid(row=2, column=len(self.checkboxes)-1, padx=(20, 20), sticky='we')

        for i in range(len(self.checkboxes)):
            self.grid_columnconfigure(i, weight=1)

        self.password_field = customtkinter.CTkEntry(self, width=30)
        self.password_field.grid(row=3, column=0, padx=(10, 20), sticky='nsew', columnspan=len(self.checkboxes))

        self.password_length_slider.set(20)
        self.password_length_entry.insert(0, 20)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(index=0, string=int(value))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password generator app")
        self.geometry("570x330")
        self.resizable(True, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.values = ["0-9", "a-z", "A-Z", "@#$%", "Startswith letter"]
        self.generated_current = False

        self.logo = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(647, 71))
        self.logo_label = customtkinter.CTkLabel(self, text='', image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.checkbox_frame_1 = SettingsFrame(self, values=self.values,
                                              title="Settings")
        self.checkbox_frame_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="wnes")

        self.button = customtkinter.CTkButton(self, text="Generate password", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=3, sticky="ew")

        self.button2 = customtkinter.CTkButton(self, text="Copy password to clipboard", command=self.copy_password)
        self.button2.grid(row=3, column=0, padx=10, pady=3, sticky="ew")

    def button_callback(self):
        values = self.checkbox_frame_1.get()
        password = create_new(length=int(self.checkbox_frame_1.password_length_entry.get()),
                              values=values)
        self.checkbox_frame_1.password_field.delete(0, "end")
        self.checkbox_frame_1.password_field.insert(0, password)
        self.generated_current = True
        self.button2.configure(text="Copy password to clipboard")

    def copy_password(self):
        if self.generated_current:
            pyperclip.copy(self.checkbox_frame_1.password_field.get())
            self.button2.configure(text="Password copied!")
            self.generated_current = False
        else:
            pyperclip.copy(self.checkbox_frame_1.password_field.get())


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
