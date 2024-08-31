import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

MAX_PASSWORD_LENGTH = 32  # Максимальна довжина пароля

# Функція для генерації пароля
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0 or length > MAX_PASSWORD_LENGTH:
            raise ValueError(tooltip_text)
    except ValueError as e:
        messagebox.showwarning(warning_title, str(e))
        return

    include_upper = upper_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Функція для копіювання пароля
def copy_password():
    password = result_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(copy_title, copy_message)

# Функція для зміни мови
def change_language(lang):
    global tooltip_text, warning_title, copy_title, copy_message
    if lang == 'EN':
        root.title("Password Generator")
        length_label.config(text="Password Length:")
        upper_check.config(text="Include Uppercase Letters")
        digits_check.config(text="Include Digits")
        special_check.config(text="Include Special Characters")
        generate_button.config(text="Generate Password")
        copy_button.config(text="Copy Password")
        tooltip_text = "Max length: 32 characters"
        warning_title = "Invalid Input"
        copy_title = "Copy"
        copy_message = "Password copied to clipboard"
    elif lang == 'UA':
        root.title("Генератор паролів")
        length_label.config(text="Довжина пароля:")
        upper_check.config(text="Включати великі літери")
        digits_check.config(text="Включати цифри")
        special_check.config(text="Включати спеціальні символи")
        generate_button.config(text="Згенерувати пароль")
        copy_button.config(text="Копіювати пароль")
        tooltip_text = "Максимальна довжина: 32 символи"
        warning_title = "Невірне значення"
        copy_title = "Копіювання"
        copy_message = "Пароль скопійовано в буфер обміну"
    elif lang == 'SK':
        root.title("Generátor hesiel")
        length_label.config(text="Dĺžka hesla:")
        upper_check.config(text="Zahrnúť veľké písmená")
        digits_check.config(text="Zahrnúť číslice")
        special_check.config(text="Zahrnúť špeciálne znaky")
        generate_button.config(text="Vygenerovať heslo")
        copy_button.config(text="Kopírovať heslo")
        tooltip_text = "Maximálna dĺžka: 32 znakov"
        warning_title = "Neplatný vstup"
        copy_title = "Kopírovanie"
        copy_message = "Heslo bolo skopírované do schránky"

# Функція для валідації введення лише чисел
def validate_numeric_input(value_if_allowed):
    if value_if_allowed.isdigit() or value_if_allowed == "":
        return True
    return False

# Показ підказки при наведенні
def show_tooltip(event):
    tooltip_label.place(x=event.x_root - root.winfo_x() + 10, y=event.y_root - root.winfo_y() + 10)
    tooltip_label.config(text=tooltip_text)

# Приховування підказки
def hide_tooltip(event):
    tooltip_label.place_forget()

# Створення головного вікна
root = tk.Tk()
root.title("Генератор паролів")
root.geometry("700x500")
root.configure(bg="#2c2c2c")

# Конфігурація валідації
vcmd = (root.register(validate_numeric_input), '%P')

# Створення та розміщення елементів інтерфейсу
length_label = tk.Label(root, text="Довжина пароля:", bg="#2c2c2c", fg="white", font=("Arial", 16, "bold"))
length_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')
length_entry = tk.Entry(root, bg="#3c3f41", fg="white", font=("Arial", 16), validate="key", validatecommand=vcmd)
length_entry.grid(row=0, column=1, padx=20, pady=20, sticky='w')

upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

upper_check = tk.Checkbutton(root, text="Включати великі літери", variable=upper_var, bg="#2c2c2c", fg="white", selectcolor="orange", activebackground="#2c2c2c", activeforeground="white", font=("Arial", 16))
upper_check.grid(row=1, column=0, columnspan=2, pady=10, sticky='w')
digits_check = tk.Checkbutton(root, text="Включати цифри", variable=digits_var, bg="#2c2c2c", fg="white", selectcolor="orange", activebackground="#2c2c2c", activeforeground="white", font=("Arial", 16))
digits_check.grid(row=2, column=0, columnspan=2, pady=10, sticky='w')
special_check = tk.Checkbutton(root, text="Включати спеціальні символи", variable=special_var, bg="#2c2c2c", fg="white", selectcolor="orange", activebackground="#2c2c2c", activeforeground="white", font=("Arial", 16))
special_check.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')

generate_button = tk.Button(root, text="Згенерувати пароль", command=generate_password, bg="#00bfae", fg="white", relief="flat", activebackground="#00a89e", font=("Arial", 16, "bold"))
generate_button.grid(row=4, column=0, padx=20, pady=20, sticky='w')
copy_button = tk.Button(root, text="Копіювати пароль", command=copy_password, bg="#00bfae", fg="white", relief="flat", activebackground="#00a89e", font=("Arial", 16, "bold"))
copy_button.grid(row=4, column=1, padx=20, pady=20, sticky='w')

# Додавання ліній під кнопками
line_separator = tk.Frame(root, height=2, bd=1, relief="solid", bg="#00bfae")
line_separator.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky='we')

result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#2c2c2c", fg="#00bfae")
result_label.grid(row=6, column=0, columnspan=2, padx=20, pady=20, sticky='w')

# Додавання підказки
tooltip_label = tk.Label(root, text="", bg="#333333", fg="white", font=("Arial", 12, "italic"))
length_entry.bind("<Enter>", show_tooltip)
length_entry.bind("<Leave>", hide_tooltip)

# Додавання кнопок для зміни мови
language_frame = tk.Frame(root, bg="#2c2c2c")
language_frame.grid(row=7, column=0, columnspan=2, pady=20, sticky='w')
tk.Button(language_frame, text="EN", command=lambda: change_language('EN'), bg="#00bfae", fg="white", relief="flat", activebackground="#00a89e", font=("Arial", 16, "bold")).pack(side="left", padx=10)
tk.Button(language_frame, text="UA", command=lambda: change_language('UA'), bg="#00bfae", fg="white", relief="flat", activebackground="#00a89e", font=("Arial", 16, "bold")).pack(side="left", padx=10)
tk.Button(language_frame, text="SK", command=lambda: change_language('SK'), bg="#00bfae", fg="white", relief="flat", activebackground="#00a89e", font=("Arial", 16, "bold")).pack(side="left", padx=10)

# Запуск основного циклу програми
tooltip_text = "Максимальна довжина: 32 символи"
warning_title = "Невірне значення"
copy_title = "Копіювання"
copy_message = "Пароль скопійовано в буфер обміну"

root.mainloop()


