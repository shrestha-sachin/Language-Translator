# Language Translator

#### Video Demo: <https://youtu.be/Ezjd3myC9ZA?si=OKuz8oVp4rUL_wRZ>

Welcome to the Language Translator project! This is a language translator project  that allows users to translate text to different languages, detect the language of a given text, view translation history, and edit saved translations. The application integrates the Google Translate API for language translation and provides a command-line interface for user interaction. Users can enter the text to be translated, specify the target language, save the translated text to a file, and download the saved files. It also includes functionality for detecting the language of a given text and viewing/editing the translation history.

### Prerequisites
Before running the program, make sure you have Python installed on your system.

## Install required dependencies
pip install googletrans==4.0.0-rc1

### Features
# 1. Translate Text
    Translate any text to the desired target language by entering the text and the target language code.

# 2. Detect Language
    Enter text, and the program will detect and display the language of the entered text.

# 3. View History
    Browse and view the history of translated texts. Select a file to view its content.

# 4. Edit History
    Edit the content of previously translated texts. Choose a file to edit and provide the new text.

# 5. Exit
    Quit the program.

### Additional Notes
Translated texts can be saved to text files with an option to download them.
Translation history files are stored in the project directory with names starting with "translated_text_" and ending with ".txt".

### Acknowledgments
Special thanks to the developers of the googletrans library.
Happy translating!
