import difflib
import tkinter as tk
from tkinter import filedialog, messagebox

def load_file(entry_widget):
    """Open a file dialog and update the entry field with the file path."""
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def calculate_similarity():
    """Calculate similarity between two text files using difflib."""
    file1_path = entry1.get()
    file2_path = entry2.get()

    if not file1_path or not file2_path:
        messagebox.showwarning("Warning", "Please select both files!")
        return

    try:
        with open(file1_path, "r", encoding="utf-8") as file1, open(file2_path, "r", encoding="utf-8") as file2:
            text1 = file1.read()
            text2 = file2.read()

        # Compare similarity using difflib
        similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
        similarity_percentage = similarity_ratio * 100

        result_label.config(text=f"Plagiarism Detected: {similarity_percentage:.2f}%", fg="blue")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create Tkinter GUI
root = tk.Tk()
root.title("Plagiarism Detector")
root.geometry("500x300")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Select First File:").pack(pady=5)
entry1 = tk.Entry(root, width=50)
entry1.pack()
tk.Button(root, text="Browse", command=lambda: load_file(entry1)).pack(pady=5)

tk.Label(root, text="Select Second File:").pack(pady=5)
entry2 = tk.Entry(root, width=50)
entry2.pack()
tk.Button(root, text="Browse", command=lambda: load_file(entry2)).pack(pady=5)

tk.Button(root, text="Check Plagiarism", command=calculate_similarity, bg="green", fg="white").pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
