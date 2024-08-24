import string

def count_words(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return len(words)

def count_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            if text.strip():
                return count_words(text)
            else:
                print("Error: The file is empty.")
                return None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main():
    while True:
        print("\nWord Count Tool")
        print("1. Input text manually")
        print("2. Load text from a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter your text: ")
            if text.strip():
                word_count = count_words(text)
                print(f"Word Count: {word_count}")
            else:
                print("Error: No text provided.")
        
        elif choice == '2':
            file_path = input("Enter the file path: ")
            word_count = count_words_from_file(file_path)
            if word_count is not None:
                print(f"Word Count: {word_count}")
        
        elif choice == '3':
            print("Thank you for using the Word Count Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
