import func
from tkinter import ttk
import os
import tkinter as tk

root = tk.Tk()
n = ttk.Notebook(root)
page1 = ttk.Frame(n)
page2 = ttk.Frame(n) 

n.add(page1, text='Encrypter')
n.add(page2, text='Decrypter')
n.pack(expand=1, fill="both")

root.title("Encrypter And Decrypter")
root.geometry("400x300")

# --- PESTAÑA 1: ENCRYPTER (Variables únicas) ---
text_encode = tk.Text(page1, height=1, width=15, font=("Helvetica", 16))
text_encode.pack(pady=20)
button_encode = tk.Button(page1, text="Encode", command=lambda: encode_button_clicked())
button_encode.pack(pady=10)
result_label_encode = tk.Label(page1, text="", wraplength=350, font=("Helvetica", 16))
result_label_encode.pack(pady=10)

# --- PESTAÑA 2: DECRYPTER (Variables únicas) ---
text_decode = tk.Text(page2, height=1, width=15, font=("Helvetica", 16))
text_decode.pack(pady=20)
button_decode = tk.Button(page2, text="Decode", command=lambda: decode_button_clicked())
button_decode.pack(pady=10)
result_label_decode = tk.Label(page2, text="", wraplength=350, font=("Helvetica", 16))
result_label_decode.pack(pady=10)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def decode(encoded):
    to_decode = ""
    for char in range(0, int(len(encoded)), 2):
        if encoded[char:char+2] in func.decode:
            to_decode = to_decode + func.decode[encoded[char:char+2]]
        else:
            print("Error")
    return to_decode

def encode(to_encode):
    encoded = ""
    for char in range(len(to_encode)):
        if to_encode[char] in func.code:
            encoded = encoded + func.code[to_encode[char]]
        else:
            print("Error")
    return encoded

# Call this function and pass the string you want to copy
def copy_to_clipboard(text_to_copy):
    root.clipboard_clear()  # Clear the current clipboard content
    root.clipboard_append(text_to_copy)  # Append the new text
    root.update()  # Keeps the text in clipboard after the window updates


# --- FUNCIONES DE LOS BOTONES ACTUALIZADAS ---
def encode_button_clicked():
    # Lee de text_encode
    input_text = text_encode.get("1.0", "end-1c")
    encoded_text = encode(input_text)
    
    if encoded_text == "":
        result_label_encode.config(text="")
    else:
        result_label_encode.config(text="Encoded string: " + encoded_text)
        copy_to_clipboard(encoded_text)  # Copia el texto codificado al portapapeles

def decode_button_clicked():
    # Lee de text_decode
    input_text = text_decode.get("1.0", "end-1c")
    decoded_text = decode(input_text)
    
    if decoded_text == "":
        result_label_decode.config(text="")
    else:
        result_label_decode.config(text="Decoded string: " + decoded_text)
        copy_to_clipboard(decoded_text)  # Copia el texto descodificado al portapapele

root.mainloop()
