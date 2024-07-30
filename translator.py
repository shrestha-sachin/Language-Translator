from googletrans import Translator, LANGUAGES
import os
from datetime import datetime


def main():
    print("========================================")
    print("|  Welcome to the Language Translator!  |")
    print("========================================")

    while True:
        print("\nOptions:\n")
        print("1. Translate Text")
        print("2. Detect Language")
        print("3. View History")
        print("4. Edit History")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            translate_option()
        elif choice == '2':
            detect_option()
        elif choice == '3':
            view_history_option()
        elif choice == '4':
            edit_history_option()
        elif choice == '5':
            print("Goodbye! See you next time!")
            break
        else:
            print("\n-------------------------------------------------------")
            print("Invalid choice! Please enter a number between 1 and 5.")
            print("-------------------------------------------------------\n")


def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def translate_option():
    user_input = input("Enter text to translate: \n")
    target_language = input("Enter target language code (e.g., 'ne' for Nepali): \n")

    try:
        if validate_language_code(target_language):
            translated_text = translate_text(user_input, target_language)
            print("\n==========================================")
            print(f"Translated text: {translated_text}")
            print("==========================================\n")

            save_option = input("Do you want to save the translated text? (Press 'S' to save, any other key to continue): ")
            if save_option.lower() == 's':
                saved_file_name = save_to_file(translated_text)
                print(f"\nTranslated text saved to '{saved_file_name}'\n")
                download_file(saved_file_name)

        else:
            print("\n----------------------------------------------------------")
            print("Invalid language code! Please enter a valid language code.")
            print("----------------------------------------------------------\n")

    except Exception as e:
        print(f"\nError: {e}\n")


def detect_option():
    user_input = input("Enter text to detect language: \n")

    try:
        translator = Translator()
        detected_language = translator.detect(user_input).lang
        print(f"\nDetected language: {LANGUAGES.get(detected_language, 'Unknown')}\n")

    except Exception as e:
        print(f"\nError: {e}\n")


def view_history_option():
    history_files = [f for f in os.listdir() if f.startswith('translated_text_') and f.endswith('.txt')]

    if not history_files:
        print("\n------------------------------")
        print("No translation history found.")
        print("------------------------------\n")
        return

    print("Available history files:")
    for i, file in enumerate(history_files, 1):
        print(f"{i}. {file}")

    while True:
        file_number = input("Select a file number to view (or enter 0 to cancel): \n")

        if file_number == '0':
            print("********************")
            print("Operation canceled.")
            print("********************")
            return

        try:
            file_number = int(file_number)
            selected_file = history_files[file_number - 1]

            with open(selected_file, 'r', encoding='utf-8') as file:
                file_content = file.read()
                print(f"\nFile Content:\n{file_content}\n")
                break
        except (ValueError, IndexError):
            print("\n-------------------------------------------------------------------")
            print("Invalid selection. Please enter a valid file number or 0 to cancel.")
            print("-------------------------------------------------------------------\n")


def edit_history_option():
    history_files = [f for f in os.listdir() if f.startswith('translated_text_') and f.endswith('.txt')]

    if not history_files:
        print("\n------------------------------")
        print("No translation history found.")
        print("------------------------------\n")
        return

    print("Available history files:")
    for i, file in enumerate(history_files, 1):
        print(f"{i}. {file}")

    while True:
        file_number = input("Select a file number to edit (or enter 0 to cancel): ")

        if file_number == '0':
            print("********************")
            print("Operation canceled.")
            print("********************")
            return

        try:
            file_number = int(file_number)
            selected_file = history_files[file_number - 1]

            with open(selected_file, 'r', encoding='utf-8') as file:
                file_content = file.read()

            edited_content = input(f"\nEdit the text:\n{file_content}\n")

            with open(selected_file, 'w', encoding='utf-8') as file:
                file.write(edited_content)
            print("File successfully edited.\n")
            break
        except (ValueError, IndexError):
            print("\n-------------------------------------------------------------------")
            print("Invalid selection. Please enter a valid file number or 0 to cancel.")
            print("-------------------------------------------------------------------\n")


def get_supported_languages():
    return list(LANGUAGES.values())


def validate_language_code(language_code):
    return language_code.lower() in [code.lower() for code in LANGUAGES.keys()]


def save_to_file(text):
    user_provided_filename = input("Enter a filename for the saved text (or press Enter to generate a unique filename): ")

    if user_provided_filename:
        file_name = f"translated_text_{user_provided_filename}.txt"
    else:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"translated_text_{timestamp}.txt"

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)

    return file_name


def download_file(file_name):
    if os.path.exists(file_name):
        print(f"\nFile 'translated_text_{file_name}' is available for download.")
        download_option = input("Do you want to download the file? (Press 'D' to download, any other key to skip): \n")
        if download_option.lower() == 'd':
            with open(file_name, 'r', encoding='utf-8') as file:
                file_content = file.read()
                print(f"\nFile Content:\n{file_content}\n")
        else:
            print("*******************")
            print("Download Skipped!")
            print("*******************")
    else:
        print("\n-----------------------------------")
        print("File not found. Unable to download.")
        print("-----------------------------------\n")


if __name__ == "__main__":
    main()
