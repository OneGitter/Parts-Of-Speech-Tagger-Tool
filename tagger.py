import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def annotate_words():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        words = file.read().split()
        annotated_words = []
        for word in words:
            tag = tag_dialog(word)
            annotated_words.append((word, tag))
    with open("annotated_words.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Tag"])
        writer.writerows(annotated_words)
    messagebox.showinfo("Annotation Completed", "Words have been annotated successfully.")

def tag_dialog(word):
    root = tk.Tk()
    tag = None
    def set_tag(selected_tag):
        nonlocal tag
        tag = selected_tag
        root.destroy()
        return tag
    tk.Label(root, text=f"Enter tag for the word '{word}':").pack()
    tk.Button(root, text="Noun", command=lambda: set_tag("Noun")).pack()
    tk.Button(root, text="Pronoun", command=lambda: set_tag("Pronoun")).pack()
    root.mainloop()
    return tag


root = tk.Tk()
root.title("Word Annotation")
root.geometry("200x200")

button = tk.Button(root, text="Annotate Words", command=annotate_words)
button.pack()

root.mainloop()
