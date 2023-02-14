import csv

def annotate_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        annotated_words = []
        for word in words:
            tag = input(f"Enter tag for the word '{word}': ")
            annotated_words.append((word, tag))
    with open("annotated_words.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Tag"])
        writer.writerows(annotated_words)

file_path = input("Enter the file path: ")
annotate_words(file_path)
