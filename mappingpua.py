import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


REPLACEMENTS1 = {

    '': 'и',
    '': 'ч',
    '': 'ѥ',
    '': 'н',


    '': ':~',

    '': '~',

    'ⷣ': 'ⷦ҇',
    '': '̅',

    '': '҆̀',

    '': 'ⷮ',   

    '': 'ᲈ',

    '': 'Ч',

    '': 'ꙋ',


    '': 'чᲈ',

    '': '҅́',  

    '': '꙾',
    '': 'ⷮ',



    '': '҆́',



    'ⷭⷭ': '҇',

    '': '҆́',



    '': 'н҇',

    '': 'ꙶ',

    '': 'оу',
    '': 'ꙁ',
    '': 'ꙑ',
    '': 'ⱑ',
    '': 'с',
    '': 'Ѱ',
    '': 'Ы',
    '': 'ⱉ',
    '': 'ч',
    '': '͡',

    '': '҃',

    'ⷣ': 'ⷣ҇',

    'ⷮ': 'ⷮ҇',

    'ⷯ': 'ⷯ҇',
    '': 'ꙩ́',

    'ⷤ҆': 'ⷤ҇',

    '': '',  


    '': '҃',

    '': '꙯',

    '': '҃',

    '': '҇',

}


REPLACEMENTS2 = {
    '0': '́',
    '1': '́',
    '2': '̀',
    '3': '҆',
    '4': '҆́',
    '5': '҆̀',
    '6': '̑',

    '7': '҃',
    '8': 'ⸯ',
    '9': 'Җ҃',
    '™': '҃'
}


def apply_mapping(text, mapping):
    
    for old_char, new_char in mapping.items():
        text = text.replace(old_char, new_char)
    return text


def process_text(input_text, mapping):
    return apply_mapping(input_text, mapping)


def process_folder(input_folder, output_folder, mapping):
    os.makedirs(output_folder, exist_ok=True)
    txt_files = glob.glob(os.path.join(input_folder, '*.txt'))
    for input_file_path in txt_files:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
        mapped_text = apply_mapping(input_text, mapping)
        file_name = os.path.basename(input_file_path)
        output_file_path = os.path.join(output_folder, file_name)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(mapped_text)


def paste_text_handler():
    selected_db = db_var.get()
    if selected_db == 'Cyrillomethodiana':
        mapping = REPLACEMENTS1
    elif selected_db == 'Азбука веры':
        mapping = REPLACEMENTS2
    else:
        messagebox.showinfo('Info', 'Work in progress for the selected database.')
        return

    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        mapped_text = process_text(input_text, mapping)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, mapped_text)
    else:
        messagebox.showwarning("Warning", "Please paste text to process.")


def select_folder_handler():
    selected_db = db_var.get()
    if selected_db == 'Cyrillomethodiana':
        mapping = REPLACEMENTS1
    elif selected_db == 'Азбука веры':
        mapping = REPLACEMENTS2
    else:
        messagebox.showinfo('Info', 'Work in progress for the selected database.')
        return

    input_folder = filedialog.askdirectory(title="Select Folder with Input Files")
    output_folder = filedialog.askdirectory(title="Select Folder for Output Files")
    if input_folder and output_folder:
        try:
            process_folder(input_folder, output_folder, mapping)
            messagebox.showinfo("Success", f"Files have been processed and saved to {output_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please select both input and output folders.")


app = tk.Tk()
app.title("PUA Handling System for Old Church Slavonic")
app.geometry("820x620")
app.resizable(False, False)


style = ttk.Style(app)
style.theme_use('clam')
style.configure('TFrame', background='#f7f7f7')
style.configure('TLabel', background='#f7f7f7', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10), padding=5)
style.configure('TCombobox', font=('Arial', 10))

main = ttk.Frame(app, padding=15)
main.pack(fill=tk.BOTH, expand=True)

# Dropdown for selecting mapping database
values = ["Cyrillomethodiana", "Азбука веры", "database 3"]
db_label = ttk.Label(main, text="Please select your desired option to convert text:")
db_label.grid(row=0, column=0, sticky='w', pady=(0,5))
db_var = tk.StringVar(value=values[0])
db_combo = ttk.Combobox(main, textvariable=db_var, state='readonly', values=values)
db_combo.grid(row=0, column=1, sticky='ew', padx=(10,0))

welcome_label = ttk.Label(
    main,
    text="Welcome to the PUA Handling System for the Conversion of Text Corpora in Old Church Slavonic",
    wraplength=600,
    font=("Arial", 12, "bold")
)
welcome_label.grid(row=1, column=0, columnspan=2, pady=(10,20))

# Text input area
input_label = ttk.Label(main, text="Paste your text below:")
input_label.grid(row=2, column=0, columnspan=2, sticky='w')
input_box = tk.Text(main, height=10, width=80, font=('Consolas', 10))
input_box.grid(row=3, column=0, columnspan=2, pady=5)
submit_text_button = ttk.Button(main, text="Submit", command=paste_text_handler)
submit_text_button.grid(row=4, column=0, columnspan=2, pady=10)

# Output area
output_label = ttk.Label(main, text="Processed Text:")
output_label.grid(row=5, column=0, columnspan=2, sticky='w')
output_box = tk.Text(main, height=10, width=80, font=('Consolas', 10))
output_box.grid(row=6, column=0, columnspan=2, pady=5)

# Folder processing
folder_label = ttk.Label(main, text="Convert an entire folder of text files:")
folder_label.grid(row=7, column=0, columnspan=2, sticky='w', pady=(20,5))
convert_folder_button = ttk.Button(main, text="Select Folder and Process", command=select_folder_handler)
convert_folder_button.grid(row=8, column=0, columnspan=2)

main.columnconfigure(1, weight=1)
main.rowconfigure(3, weight=1)
main.rowconfigure(6, weight=1)

app.mainloop()
