#Task 1

This Python code demonstrates how to safely read specific lines from a text file using exception handling. It tries to open a file named **`sample.txt`** in read mode (`'r'`). If the file exists, it uses the `readline()` method twice to read and print the first two lines one by one, labeling them as “Line 1” and “Line 2” in the output. After reading, it closes the file to free system resources. However, if **`sample.txt`** does not exist in the directory, the `open()` function raises a `FileNotFoundError`. In that case, the `except` block catches this error and prints a user-friendly message: *“The File 'sample.txt' not found”*. This ensures that the program doesn’t crash unexpectedly if the file is missing, and gives clear feedback to the user instead.

#Task2

Here’s a clear **description** of your updated code in **one paragraph**:

This Python program demonstrates how to write, append, and read text data from a file named **`output.txt`** using file handling techniques. First, it opens the file in **read and write mode (`r+`)**, takes user input, and writes that input to the file, overwriting any existing content. After closing the file, it reopens the same file in **append mode (`a`)**, takes additional input from the user, and writes it to the file, but this time it prepends a newline character (`\n`) to ensure the new text appears on a new line instead of being merged with the previous text. After appending, it closes the file again. Finally, it opens the file in **read mode (`r+`)** to read all the contents of **`output.txt`** and displays the complete text on the console, allowing the user to verify that both the written and appended data have been stored correctly.

