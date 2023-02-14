Part Of Speech Tagging Tool

This is a Python program that allows the user to annotate words with their corresponding parts of speech. The annotated words are stored in a CSV file.

How to use
Run the program using the command python annotate_words.py or by running the script from an IDE like PyCharm.
Click the "Annotate Words" button to open a file dialog box.
Select the text file containing the words you want to annotate.
For each word, a dialog box will appear asking you to select the tag that corresponds to its part of speech. You can choose between "Noun" and "Pronoun".
The annotated words will be saved in a CSV file named "annotated_words.csv" in the same directory as the program.
A message box will appear indicating that the annotation process has been completed.
Dependencies
The program requires the following dependencies:

tkinter for creating the user interface
csv for reading and writing CSV files
Notes
The program assumes that the text file contains one word per line.
The program uses a simple dialog box to prompt the user for the part of speech tag. If you need to add more tags or use a different tagging scheme, you will need to modify the tag_dialog function in the code.
The program was last updated in February 2023 and tested in Python 3.9.7.
