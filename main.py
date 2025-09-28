import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols, exclude_chars):
    # Define character sets
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Remove excluded characters
    for char in exclude_chars:
        chars = chars.replace(char, '')

    if not chars:
        raise ValueError("No characters available for password generation. Please select at least one character type and check excluded characters.")

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive.")
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        exclude_chars = exclude_entry.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols, exclude_chars)
        password_label.config(text=password)
        copy_button.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_copy():
    password = password_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(True, True)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)
root.rowconfigure(3, weight=0)
root.rowconfigure(4, weight=0)
root.rowconfigure(5, weight=0)
root.rowconfigure(6, weight=0)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=0)

# Length input
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
length_entry.insert(0, "12")

# Character type checkboxes
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=2)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=2)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=2)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=2)

# Exclude characters
tk.Label(root, text="Exclude Characters:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
exclude_entry = tk.Entry(root, width=20)
exclude_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Password display
tk.Label(root, text="Generated Password:").grid(row=7, column=0, sticky="w", padx=10, pady=5)
password_label = tk.Label(root, text="", font=("Courier", 12), bg="white", relief="sunken", wraplength=300)
password_label.grid(row=7, column=1, sticky="nsew", padx=10, pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy, state=tk.DISABLED)
copy_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
