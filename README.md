# Bookbot

## Overview
This Python script provides a simple yet effective way to analyze the contents of a book. It reads a text file containing the book's content, counts the total number of words, and provides a frequency count of each character (alphabetical characters only). The results are sorted in descending order based on the frequency of each character.

## Features
- **Word Count:** Calculates the total number of words in the book.
- **Character Frequency Analysis:** Counts how often each alphabetical character appears in the text and sorts them by frequency.

## How to Use
1. Ensure you have Python installed on your system.
2. Place the book file (a `.txt` file) in the `books` directory. The current script is set up to analyze `books/frankenstein.txt`.
3. Run the script using the command: `python main.py`.
4. The script will print a report in the console, starting with the path to the book, followed by the total word count, and then the frequency of each character.

## Customization
To analyze a different book, change the `path` variable in the `main()` function to the path of your book file.

## Requirements
- Python 3.x

## License
This project is open source and available under the [MIT License](LICENSE).  
Books used are free licensed copies publically available.