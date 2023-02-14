import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

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
    class TagDialog(simpledialog.Dialog):
        def body(self, master):
            tk.Label(master, text=f"Enter tag for the word '{word}':").grid(row=0, column=0, padx=5, pady=5)
            self.tag = tk.StringVar()
            tk.Radiobutton(master, text="Noun", variable=self.tag, value="Noun").grid(row=1, column=0, padx=5, pady=5)
            tk.Radiobutton(master, text="Pronoun", variable=self.tag, value="Pronoun").grid(row=2, column=0, padx=5, pady=5)
            return None
        def apply(self):
            self.result = self.tag.get()
    tag = TagDialog(root).result
    return tag

root = tk.Tk()
root.title("Word Annotation")
root.geometry("1920x1080")

button = tk.Button(root, text="Annotate Words", command=annotate_words)
button.pack()

root.mainloop()
